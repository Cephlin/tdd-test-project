# pylint: disable=C0111
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # pylint: disable=C0103
    def test_can_start_a_list_and_retrieve_it_later(self):

        self.a_new_user_visits_the_homepage()
        self.user_notices_the_title_and_header()

        inputbox = self.she_can_enter_a_new_item_in_the_list_straight_away()
        self.she_enters_eat_pizza_into_the_textbox(inputbox)
        # self.pressing_enter_updates_the_todo_list_with_first_item(inputbox)

        # She can still add new items via a text box so she enters "Clean up
        # after pizza"
        # self.fail("Finish the test!")

        # The page is updated to show both entries on the screen with the new one being
        # second.

        # She wants to save the list for future and notices that the site has created
        # a unique link with a brief explanation.

        # She tries out the URL just to be sure it works and it does

    def a_new_user_visits_the_homepage(self):

        self.browser.get('http://localhost:8000')

    def user_notices_the_title_and_header(self):

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

    def she_can_enter_a_new_item_in_the_list_straight_away(self):

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        return inputbox

    def she_enters_eat_pizza_into_the_textbox(self, inputbox):

        inputbox.send_keys('Eat pizza')

    def pressing_enter_updates_the_todo_list_with_first_item(self, inputbox):

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Eat pizza' for row in rows)
        )


if __name__ == '__main__':
    unittest.main(warnings='ignore')
