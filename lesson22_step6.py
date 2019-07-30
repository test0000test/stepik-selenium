from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

res = calc(int(browser.find_element_by_id("input_value").text))
browser.find_element_by_id("answer").send_keys(res)

chk = browser.find_element_by_id("robotCheckbox")
browser.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", chk)

rd = browser.find_element_by_id("robotsRule")
browser.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", rd)

btn = browser.find_element_by_css_selector("button.btn")
browser.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", btn)