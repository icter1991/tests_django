from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Ninja\PycharmProjects\geckodriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała się o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia.
        # Postanowila wiec przejsc na strone glowna tej aplikacji.
        self.browser.get('http://localhost:8000')

        # Zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy.
        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.fail('Listy', header_text)

        # Od razu zostaje zachecona, aby wpisac rzecz do zrobienia.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Wpisz rzecz do zrobienia')

        # W polu tekstowym wpisala "Kupic pawie piora"(hobby Edyty
        # polega na tworzeniu ozdobnych przynent).
        inputbox.send_keys('Kupic pawie piora')

        # Po nacisnieciu klawisza Enter strona zostala uaktualniona i wyswietla
        # "1: Kupic pawie piora" jako element listy rzeczy do zrobienia.
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Kupic pawie piora' for row in rows))

        # Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnego zadania.
        # Edyta wpisala "Uzyc pawich pior do zrobienia przynety" (Edyta jest niezwykle skrupulatna).
        self.fail('Zakonczenie testu!')

    # Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia.

    # Edyta byla ciekawa, czy witryna zapamieta jej liste. Zwrocila uwage na wygenerowany dla niej
    # unikatowy adres URL, obok ktorego znajduje sie pewien tekst z wyjasnieniem.

    # Przechodzi pod podany adres URL i widzi wyswietlona swoja liste rzeczy do zrobienia.

    # Usatysfakcjonowana kladzie sie spac.

if __name__ == '__main__':
    unittest.main()

browser.quit()