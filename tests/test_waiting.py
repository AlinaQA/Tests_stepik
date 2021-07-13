import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    element = browser.find_element_by_css_selector("#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    x_element = element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x_element))

    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    print(browser.switch_to.alert.text) # Ответ
    browser.quit()