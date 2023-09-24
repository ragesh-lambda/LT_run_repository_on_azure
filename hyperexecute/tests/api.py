import os
import unittest
import sys
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestLoader, TestSuite
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner
import time
import requests

# Username and AccessKey available at https://accounts.lambdatest.com/detail/profile
username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

# Get the Present Working Directory since that is the place where the report
# would be stored
current_directory = os.getcwd()

class HyperTestPyUnitTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build": '[Python] [Test Scenario-1] HyperTest demo using PyUnit framework',
            "name": '[Python] [Test Scenario-1] HyperTest demo using PyUnit framework',
            "platform": os.environ.get("TARGET_OS"),
            "browserName": 'chrome',
            "version": 'latest'
        }
        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
    #driver = self.driver
#/html/body/div[6]/div/ul/li[2]/a/div/span

        self.driver.get("http://cyclos-demo.lambdatestinternal.com/demo/classic")

        # set the API endpoint URL
        #url = "http://cyclos-demo.lambdatestinternal.com/api/John/accounts"

        # set the headers if needed
        #headers = {'Content-Type': 'application/json'}

        # set the data to be sent as a request payload (if needed)
        #data = {"name": "John Doe", "email": "johndoe@example.com"}

        # send a GET request to the API endpoint
        #response = requests.get(url, headers=headers)

        # send a POST request to the API endpoint
        #response = requests.post(url, headers=headers, json=data)

        # send a PUT request to the API endpoint
        #response = requests.put(url, headers=headers, json=data)

        # send a DELETE request to the API endpoint
        #response = requests.delete(url, headers=headers)
        status_code = 201
        # print the response status code and response body
        print(response.status_code)
        print(response.json())

        if status_code != 200:
            self.driver.execute_script("lambda-status=failed")
        else:
            self.driver.execute_script("lambda-status=passed")





if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_1'))
