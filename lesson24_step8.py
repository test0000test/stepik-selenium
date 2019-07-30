from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)
button.click()

WebDriverWait(browser, 2).until(
	EC.element_to_be_clickable((By.ID, "solve"))
)
browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
browser.find_element_by_id("solve").click()