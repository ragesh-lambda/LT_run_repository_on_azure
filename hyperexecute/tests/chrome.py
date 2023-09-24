import datetime
import os
from typing import KeysView
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestLoader, TestSuite
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
#from runner import HTMLTestRunner
import time

# Username and AccessKey available at https://accounts.lambdatest.com/detail/profile
username = "shubhamr"
access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"

# Get the Present Working Directory since that is the place where the report
# would be stored
current_directory = os.getcwd()

class HyperTestPyUnitTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        today = datetime.date.today()
        
        desired_caps = {
            "build": 'Smoke_'+ str(today),
            "name": 'Smoke_Test',
            "browserName":os.environ.get("browser"),
            "platform": os.environ.get("TARGET_OS"),
            "version": 'latest',
            "visual":True,
            "network":True,
            "console":True
        }
        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):

        try:
            self.driver.get("https://ecommerce-playground.lambdatest.io/")
            time.sleep(12)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[5]/header/div[3]/div[1]/div/div[3]/nav/div/ul/li[3]/a/div/span").click() #clicks on blogs
            time.sleep(12)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[1]/a/img").click() #clicks on first blog
            time.sleep(20)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/div/a[4]").click()
            time.sleep(2)
            #Sign in completed
            #self.driver.find_element(By.CSS_SELECTOR, ".actionButton").click()
            time.sleep(45)
            #/html/body/ui-root/div/top-bar/nav/div/div/menus/a[2]/div
            #Click on banking
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/top-bar/nav/div/div/menus/a[2]/div").click()
            # time.sleep(3)
            # #click on payment to user
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/account-history/page-layout/div/div[1]/side-menu/div/nav/a[3]/div").click()
            # time.sleep(2)
            # #Enter user name
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/payment/page-layout/div/div[2]/page-content/div/div[2]/payment-step-form/label-value[2]/div/div/user-field/div/div[1]/div/input").send_keys("John", Keys.ARROW_DOWN)
            # time.sleep(1)
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/payment/page-layout/div/div[2]/page-content/div/div[2]/payment-step-form/label-value[2]/div/div/user-field/div/div[1]/div/div/a").click()
            # time.sleep(1)
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/payment/page-layout/div/div[2]/page-content/div/div[2]/payment-step-form/decimal-field/label-value/div/div/div/input").send_keys("100")
            # time.sleep(1)
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/payment/page-layout/div/div[2]/page-content/div/div[2]/actions/action-button/button").click()
            # time.sleep(1)
            # self.driver.find_element_by_xpath("/html/body/ui-root/div/div/payment/page-layout/div/div/page-content/div/div[2]/actions/action-button[1]/button").click()
            # time.sleep(3)
            self.driver.execute_script("lambda-status=passed")
        except:
            self.driver.execute_script("lambda-status=failed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
