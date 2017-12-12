from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Ninja\PycharmProjects\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała się o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia.
        # Postanowila wiec przejsc na strone glowna tej aplikacji.
        self.browser.get(self.live_server_url)

        # Zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Od razu zostaje zachecona, aby wpisac rzecz do zrobienia.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # W polu tekstowym wpisala "Kupic pawie piora"(hobby Edyty
        # polega na tworzeniu ozdobnych przynent).
        inputbox.send_keys('Buy peacock feathers')

        # Po nacisnieciu klawisza Enter strona zostala uaktualniona i wyswietla
        # "1: Kupic pawie piora" jako element listy rzeczy do zrobienia.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnego zadania.
        # Edyta wpisala "Uzyc pawich pior do zrobienia przynety" (Edyta jest niezwykle skrupulatna).
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make fly')

        # Edyta byla ciekawa, czy witryna zapamieta jej liste. Zwrocila uwage na wygenerowany dla niej
        # unikatowy adres URL, obok ktorego znajduje sie pewien tekst z wyjasnieniem.
        self.fail('Finish the test')

    # Przechodzi pod podany adres URL i widzi wyswietlona swoja liste rzeczy do zrobienia.

    # Usatysfakcjonowana kladzie sie spac.

