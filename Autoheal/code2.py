import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time

class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        lt_options = {
            "user": "shubhamr",
            "accessKey": "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh",
            #"build" = os.getenv("LT_BUILD_NAME")
            "build" : "Auto test2",
            #"build": "UnitTest-Selenium-Sample_Hooks_blaze",
            "name": "UnitTest-Selenium-Test1",
            "platformName": "MacOS Ventura",
            "w3c": True,
            "browserName": "Chrome",
            "tunnel": True,
            "browserVersion": "latest-2",
            # "selenium_version": "4.8.0",
            "autoHeal": True
        }
        
        browser_options = ChromeOptions()
        browser_options.set_capability('LT:Options', lt_options)
        browser_options.set_capability('autoHeal', True)
        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/


       

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)


# tearDown runs after each test case

    def tearDown(self):
        #webhooks
        #self.driver.execute_script("lambda-status=passed")
        print("passed")
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        
        driver.get("https://ritamganguli.github.io/auto_heal_web_hoast/")

        time.sleep(2)

        driver.find_element(By.ID, "testNameArea").send_keys("ADMIN")
        driver.find_element(By.ID, "txtEmailBox").send_keys("admin@lambdatest.com")

        element = driver.find_element(By.XPATH, "//textarea[@name='message']")
        element.send_keys("LamdaTest_test")

        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#phoneBox").send_keys('7789870981')
    


        driver.find_element(By.ID, "subjectArea").send_keys("Testing")
        

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='submitBtn']").click()

        time.sleep(2)

        #element = driver.find_element(By.XPATH, "//a[@id='nava']").text
        # search_text = "PRODUCT STORE"
        # if search_text in element.text:
        #     print(f"The element contains the {search_text}.")
        # else:
        #     print(f"The element does not contain the search text: {search_text}.")
        #assert element == "PRODUCT STORE"

        time.sleep(2)

        # driver.find_element(By.ID, "logout2").click()
        # time.sleep(3)

    

if __name__ == "__main__":
    unittest.main()
