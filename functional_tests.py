from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    """New visitor's test"""

    def setUp(self):
        """setup"""
        self.browser = webdriver.Chrome("../chromedriver")

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        Test to can start a new list and retrieve it later
        """
        # Edit heard about new online to-do application.
        # She decided to evaluate the homepage.
        self.browser.get("http://localhost:8000")

        # She sees that the page header and title talk about urgent to-do lists
        self.assertIn(
            "To-Do", self.browser.title
        ), f"Browser title was {self.browser.title}"
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn(
            "To-Do", header_text
        )

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a to-do item"
        )
        
        # Она набирает в текстовом поле "Buy a peacock feathers" (ее хобби –
        # вязание рыболовных мушек)
        inputbox.send_keys("Buy a peacock feathers")

        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Buy a peacock feathers" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy a peacock feathers" for row in rows)
        )

        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        self.fail("End this test!")

        # Страница снова обновляется, и теперь показывает оба элемента ее списка

        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с объяснениями.

        # Она посещает этот URL-адрес – ее список по-прежнему там.

    def tearDown(self):
        """tear down"""
        self.browser.quit()

    # Удовлетворенная, она снова ложится спать


if __name__ == "__main__":
    unittest.main(warnings="ignore")
