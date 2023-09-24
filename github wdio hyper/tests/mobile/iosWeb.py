from appium import webdriver
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "iPhone.*",
    "platformName": "ios",
    #"platformVersion": "15",
    "isRealMobile": True,
    "build": "Python Vanilla IOS",
    "name": "Sample Test - Python",
    "browserName":"Safari",
    "version":"latest",
    "network": False,
    "visual": True,
    "video": True,
    "region":"us"
}


def startingTest():

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(command_executor="https://" +
                                  "ritamg"+":"+"lHWNSA0QECwjeN8DoDb9U6KyXMBgAFXqlIIArkxeOTDSeEdLyG"+"@mobile-hub.lambdatest.com/wd/hub",desired_capabilities=desired_caps)
        driver.get("https://ecommerce-playground.lambdatest.io/")
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[5]/header/div[2]/div[2]/div[3]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/nav/div/ul/li[4]/a/div").click()
        time.sleep(30)
        driver.quit()
    except:
        driver.quit()


startingTest()