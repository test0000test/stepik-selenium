from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element_by_css_selector("button.btn").click()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))

btn = browser.find_element_by_css_selector("button.btn").click()

