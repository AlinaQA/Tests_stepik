from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(calc(x_element))
    
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()