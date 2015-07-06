from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest
import sys
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_emply_list_items(self):
        self.fail("Write me!")