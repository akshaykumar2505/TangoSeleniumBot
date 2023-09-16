import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expectedConditions, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = RequestProxy()
proxies = req_proxy.

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
options.add_argument("user-data-dir=C:\\Users\\akshay\\AppData\\Local\\Google\\Chrome Beta\\User Data")

PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,

    "proxyType": "MANUAL",

}

driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
driver.get("https://www.tango.me/stream/0PTXXZx5n1lKDdJRlqYfUA")

message = "Fak"
while True:
    wait = WebDriverWait(driver, 5)
    chat = wait.until(expectedConditions.presence_of_element_located(
        (By.XPATH, "//*[@id='root']/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/textarea")))
    chat.click()
    message = message + message
    chat.send_keys(message)
    chat.send_keys(Keys.RETURN)
    time.sleep(1)
