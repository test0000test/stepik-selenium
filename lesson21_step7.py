from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_tag_name("img").get_attribute("valuex")
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_id("robotCheckbox").click() #setAttribute("checked", "checked")
browser.find_element_by_id("robotsRule").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

#robots_radio = browser.find_element_by_id("robotsRule")
#robots_checked = robots_radio.get_attribute("checked")
#assert robots_checked is None

#assert human_checked == "true", "Human radio is not selected by default"

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
#time.sleep(1)

# находим элемент, содержащий текст
#welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
#welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text