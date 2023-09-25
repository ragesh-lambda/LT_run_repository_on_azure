import unittest
import time
from selenium import webdriver
import csv
from datetime import datetime 

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Read credentials from the CSV file
        with open('crediantial.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                username = row['username']
                accesskey = row['accesskey']
                current_datetime = datetime.now().strftime("%d-%m-%Y %H%M%S")

                # Set desired capabilities for the WebDriver
                desired_caps = {
                    "build": 'PyunitTest sample build',
                    "name": 'Py-unittest',
                    "browserName": 'Chrome',
                    "version": 'latest',
                    "platform": 'Windows 10',
                    "resolution": '1024x768',
                    "network": 'true',
                    "smartUI.project": "Smart UI Testing 125",
                    "smartUI.build": "buildName"+current_datetime,
                    "pageLoadTimeout": 30000,  # 30 seconds
                    "scriptTimeout": 300000 # 30 seconds
                }

                errorColor = {
                    "red": 255,
                    "green": 0,
                    "blue": 0
                }

                output = {
                    "errorColor": errorColor,
                    "transparency": 0.5,
                    "largeImageThreshold": 1200
                }

                sm = {
                    "output": output,
                    "scaleToSameSize": True
                }

                # Create the WebDriver instance
                self.driver = webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, accesskey),desired_capabilities=desired_caps)

    def test_example(self):
        # Your test code here
        self.driver.get("https://www.lambdatest.com/")
        time.sleep(10)
        print("Taking screenshot")
        self.driver.execute_script("smartui.takeScreenshot,{\"screenshotName\":\"ritam-screenshot-2\"}")
        print("screenshot taken successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
