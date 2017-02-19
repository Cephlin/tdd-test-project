"""Something
"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Laura has found a cool new to-do list web-app so she visits the
        # homepage
        self.browser.get('http://localhost:8000')

        # She notices the title and the header
        self.assertIn('TODO', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('TODO', header_text)

        # She can enter a new item to the list straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She enters "Eat pizza" into the textbox
        inputbox.send_keys('Eat pizza')

        # When she hits enter, the page updates with the first item in the TODO list.
        # It lists "1: Eat pizza" as the first item.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Eat pizza' for row in rows)
        )


        # She can still add new items via a text box so she enters "Clean up after pizza"
        self.fail("Finish the test!")

        # The page is updated to show both entries on the screen with the new one being
        # second.


        # She wants to save the list for future and notices that the site has created
        # a unique link with a brief explanation.


        # She tries out the URL just to be sure it works and it does

if __name__ == '__main__':
    unittest.main(warnings='ignore')
