import os
import time
from selenium import webdriver

driver_path = os.getenv('D_PATH')
browser = webdriver.Chrome(executable_path=driver_path)
link = 'http://suninjuly.github.io/registration2.html'
control_text = 'Congratulations! You have successfully registered!'
try:
    browser.get(link)
    button = browser.find_element_by_css_selector('button')
    required_fields = browser.find_elements_by_css_selector('input[required]')
    for field in required_fields:
        field.send_keys('yes')
    button.click()
    welcome_text = browser.find_element_by_css_selector('h1').text
    assert control_text == welcome_text

finally:
    time.sleep(10)
    browser.quit()
