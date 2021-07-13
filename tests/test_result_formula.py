from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_css_selector("#num1").text
    number2 = browser.find_element_by_css_selector("#num2").text
    
    summa = int(number1) + int(number2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa)) # ищем элемент с нужным текстом
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()