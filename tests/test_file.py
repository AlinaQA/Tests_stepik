import os
import time
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("stepik@mail.ru")

    current_dir = os.path.abspath(os.path.dirname("C:/Users/user/environments/"))
    print(current_dir)
    file_name = "Шпора.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()