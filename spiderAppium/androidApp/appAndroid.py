from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import twisted



server = "http://localhost:4723/wd/hub"

desired_caps = {
    "platformName": "Android",
    "deviceName": "",
    "appPackage":"",
    "appActivity":""
}

driver = webdriver.Remote(server, desired_caps)

