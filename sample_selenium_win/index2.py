import datetime
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilitie
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
import csv
from datetime import datetime
import csv

def run_automation_script(row):
    username = row[0]
    accesskey = row[1]
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Running automation script with Username: {username} and Access Key: {accesskey}")
    print("hello")
    build = ""
    gridUrl = "hub.lambdatest.com/wd/hub"
    options = ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["name"] = f"Selenium Test - {current_date}"
    lt_options["build"] = "Selenium Sample Test Windows"
    lt_options["network"] = True
    lt_options["visual"]=True
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options.set_capability('LT:Options', lt_options)
    url = "https://"+username+":"+accesskey+"@"+gridUrl
    driver = webdriver.Remote(
            command_executor=url,
            options=options
        )
    Username = "ritamg@lambdatest.com"
    pd = "lambdatest"
    Url = "https://accounts.lambdatest.com/login"
    # driver = webdriver.Chrome()
    driver.get(Url)
    uname = driver.find_element("id", "email")
    uname.send_keys(Username)
    password = driver.find_element("id", "password")
    password.send_keys(pd)
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    driver.quit()

filename = "crediantial.csv"

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  
    for row in csvreader:
        if len(row) >= 2:
            run_automation_script(row)
            print("wait")
            

print("finished")


