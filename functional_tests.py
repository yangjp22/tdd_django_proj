from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def send_keys_in_input(self, content):
        input_box = self.browser.find_element(By.ID, "id_new_item")
        input_box.send_keys(content)
        input_box.send_keys(Keys.ENTER)

    def check_for_row_in_list_table(self, row_text):
        time.sleep(0.5)
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(
            row_text, [row.text for row in rows],
            "New to-do item did not appear in table"
        )

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("To-Do lists", self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            input_box.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        self.send_keys_in_input("Buy a feather")
        self.check_for_row_in_list_table("1: Buy a feather")

        self.send_keys_in_input("Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy a feather")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        self.fail("Intentional failure 1")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
