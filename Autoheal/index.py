import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import csv
import time
import csv
from datetime import datetime


class FirstSampleTest(unittest.TestCase):

    def read_credentials_from_csv(self, csv_file):
        credentials = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                credentials.append((row['username'], row['accesskey']))
        return credentials

    def setUp(self):
        # Read credentials from CSV file
        csv_credentials = self.read_credentials_from_csv('crediantial.csv')

        self.test_cases = []
        for username, access_key in csv_credentials:
            current_time = datetime.now().strftime("%d-%m-%Y,Time: %H:%M:%S")
            test_name = f"UnitTest-Selenium-Test2-{current_time}"
            lt_options = {
                "user": username,
                "accessKey": access_key,
                "build": "Selenium Standard Test",
                "name":test_name,
                "platformName": "MacOS Ventura",
                "w3c": True,
                "browserName": "Chrome",
                "tunnel": False,
                "browserVersion": "latest-2",
                "autoHeal": True
            }

            browser_options = ChromeOptions()
            browser_options.set_capability('LT:Options', lt_options)
            browser_options.set_capability('autoHeal', True)

            self.test_cases.append((username, browser_options))

    def tearDown(self):
        pass

    def test_unit_user_should_able_to_add_item(self):
        for username, browser_options in self.test_cases:
            with self.subTest(username=username):
                driver = webdriver.Remote(
                    command_executor="http://hub.lambdatest.com:80/wd/hub",
                    options=browser_options
                )

                driver.get("https://ritamganguli.github.io/auto_heal_web_hoast/")

                time.sleep(2)

                driver.find_element(By.ID, "testNameArea").send_keys("ADMIN")
                driver.find_element(By.ID, "txtEmailBox").send_keys("admin@lambdatest.com")
                element = driver.find_element(By.ID, "textMessage")
                element.send_keys("LamdaTest_test")

                time.sleep(2)

                driver.find_element(By.ID, "txtPhone").send_keys('7789870981')
            


                driver.find_element(By.ID, "subAreaText").send_keys("Testing")
                

                time.sleep(2)

                driver.find_element(By.ID, "formSubmitBtn").click()

                time.sleep(2)

        #element = driver.find_element(By.XPATH, "//a[@id='nava']").text
        # search_text = "PRODUCT STORE"
        # if search_text in element.text:
        #     print(f"The element contains the {search_text}.")
        # else:
        #     print(f"The element does not contain the search text: {search_text}.")
        #assert element == "PRODUCT STORE"

            

                # Rest of your test logic...

                driver.quit()

if __name__ == "__main__":
    unittest.main()
