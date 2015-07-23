from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest
import sys
from unittest import skip

class NewVisitorTest(FunctionalTest):
        
    def test_can_start_a_list_and_retrieve_it_later(self):        
        #Edith has heard about a cool new online to-do app. she goes
        #to check out its homepage
        self.browser.get(self.server_url)

        #She notices the page title and header metion to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #She types "Buy peacock feathers" into a text box (Edith's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #When she hits enter, the page updates, and now the page lists
        #"1: Buy peacock feathers" as an item in to-do list
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #There is still another text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #Now a new user, Francis, came along to the site

        ## We use a new browser session to make sure no information from Edith's
        ## is coming through from cook's etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visited the home page, there is no sign of Edith's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list with his items, he is less
        # interested in Edith's
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Fancis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's url
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        

        
        #self.fail('Fail the test!')
        #The page updates again, and now shows both item in her list

        #Edith wonder whether the site will remember her list. Then she sees that
        #the site has generated a unique URL for her -- there is some
        #explanatory text to that effect

        #she visits that URL - her to-do list is still there

        #Satisfied, she goes back to sleep
