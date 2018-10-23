from selenium import webdriver
import unittest
import time


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

