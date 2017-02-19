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
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She can enter a new item to the list straight away


        # She enters "Eat pizza" into the textbox


        # When she hits enter, the page updates with the first item in the TODO list.
        # It lists "1: Eat pizza" as the first item.


        # She can still add new items via a text box so she enters "Clean up after pizza"


        # The page is updated to show both entries on the screen with the new one being
        # second.


        # She wants to save the list for future and notices that the site has created
        # a unique link with a brief explanation.


        # She tries out the URL just to be sure it works and it does

if __name__ == '__main__':
    unittest.main(warnings='ignore')
