from selenium import webdriver
import unittest


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

        # She sees that the page header talk about urgent to-do lists
        self.assertIn(
            "To-Do", self.browser.title
        ), f"Browser title was {self.browser.title}"
        self.fail("End this test")

        # Ей сразу же предлагается ввести элемент списка

        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
        # вязание рыболовных мушек)

        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка

        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)

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
