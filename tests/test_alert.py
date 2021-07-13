import time
import math
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x_element))

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    print(browser.switch_to.alert.text) # Ответ
    browser.quit()