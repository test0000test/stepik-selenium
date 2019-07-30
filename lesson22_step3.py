from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

val = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(val)) 
browser.find_element_by_css_selector("button.btn").click()

#select_by_visible_text
#select_by_index