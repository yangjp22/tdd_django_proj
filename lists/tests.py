from django.urls import resolve
from django.test import TestCase, override_settings, Client
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home


# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_math(self) -> None:
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        self.assertTrue(response.content.startswith(b"<html"))
        self.assertIn(b"<title>To-Do lists</title>", response.content)
        self.assertTrue(response.content.endswith(b"</html>"))

    @override_settings(MIDDLEWARE=[])
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "Buy a feather"

        response = home(request)
        self.assertEqual(response.status_code, 200)
