import os
import time
from selenium import webdriver

driver_path = os.getenv('D_PATH')
special_path = True 
"""В моем случае для корректной работы Chromium при инициации webdriver требуется передать исполняемый путь '/snap/bin/chromium.chromedriver'. У меня он сохранен как переменная окружения. Если с браузером проблем нет, то флаг в переменной special_path меняем на False"""
link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'
control_text = 'Congratulations! You have successfully registered!'

try:
    if special_path:
        browser = webdriver.Chrome(executable_path=driver_path)
    else:
        browser = webdriver.Chrome()
    browser.get(link_2)
    required_fields = [
            'Input your first name',
            'Input your last name',
            'Input your email'
            ]
    for field in required_fields:
        browser.find_element_by_css_selector(f"[placeholder='{field}']").send_keys('test')
    button = browser.find_element_by_css_selector('button')
    button.click()
    welcome_text = browser.find_element_by_css_selector('h1').text
    assert control_text == welcome_text

finally:
    time.sleep(5)
    browser.quit()
        
