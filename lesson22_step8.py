from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

	
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name("firstname").send_keys("test1")
browser.find_element_by_name("lastname").send_keys("test2")
browser.find_element_by_name("email").send_keys("test3")

browser.find_element_by_name("file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.txt"))

btn = browser.find_element_by_css_selector("button.btn").click()