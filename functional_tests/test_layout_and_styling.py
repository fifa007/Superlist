from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest
import sys
from unittest import skip

class LayoutAndStylingTest(FunctionalTest):
    
    def test_layout_and_styling(self):
        # Edith goes to home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She noticed the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,
                               512, delta = 5)