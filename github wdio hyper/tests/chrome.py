import datetime
import os
import csv  # Add the CSV module for reading credentials
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestLoader, TestSuite
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import time

# Get the Present Working Directory since that is the place where the report would be stored
current_directory = os.getcwd()

class HyperTestPyUnitTest(unittest.TestCase):
    def setUp(self):
        today = datetime.date.today()
        self.driver = None  # Initialize the driver

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def run_test_with_credentials(self, username, access_key):
        try:
            desired_caps = {
                "build": 'Smoke_',
                "name": 'Smoke_Test',
                "browserName": os.environ.get("browser"),
                "platform": os.environ.get("TARGET_OS"),
                "version": 'latest',
                "visual": True,
                "network": True,
                "console": True
            }
            self.driver = webdriver.Remote(
                command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
                desired_capabilities=desired_caps)

            self.driver.get("https://ecommerce-playground.lambdatest.io/")
            # Rest of your test code here...

            self.driver.execute_script("lambda-status=passed")
        except:
            if self.driver:
                self.driver.execute_script("lambda-status=failed")

    def test_unit_user_should_able_to_add_item(self):
        with open('credential.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                username = row['username']
                access_key = row['accesskey']
                self.run_test_with_credentials(username, access_key)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
