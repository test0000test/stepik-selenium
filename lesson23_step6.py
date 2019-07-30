from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("button.trollface").click()
time.sleep(1)
browser.switch_to.window(browser.window_handles[1])

browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))

browser.find_element_by_css_selector("button.btn").click()

# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
# browser.switch_to.window(window_name)