from django.urls import resolve
from django.test import TestCase


from lists.views import home


# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_math(self) -> None:
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        print(found, dir(found))
        self.assertEqual(found.func, home)
