import os
import time

from selenium import webdriver

driver_path = os.getenv('D_PATH')
link = 'http://suninjuly.github.io/simple_form_find_task.html'

browser = webdriver.Chrome(executable_path=driver_path)
try:
    browser.get(link)
    first_name = browser.find_element_by_name('first_name')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys('Petrov')
    city = browser.find_element_by_css_selector('.city')
    city.send_keys('Smolensk')
    country = browser.find_element_by_css_selector('#country')
    country.send_keys('Russia')
    button = browser.find_element_by_css_selector('#submit_button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

