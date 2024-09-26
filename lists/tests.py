from django.urls import resolve
from django.test import TestCase, override_settings, Client
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.models import Item
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


class ItemModels(TestCase):

    def save_item(self, text):
        item = Item()
        item.item_text = text
        item.save()

    def test_saving_and_retrieving_items(self):
        self.save_item("The first (ever) list item")
        self.save_item("Item the second")

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_item = saved_items[0]
        second_item = saved_items[1]
        self.assertEqual(first_item.item_text, "The first (ever) list item")
        self.assertEqual(second_item.item_text, "Item the second")
