from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

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
        input_box.send_keys("Buy peacock feathers")
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows)
        )

        self.fail("Intentional failure 1")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
