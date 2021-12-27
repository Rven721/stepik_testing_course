import os
import math
import time

from selenium import webdriver

driver_path = os.getenv('D_PATH')
link = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome(executable_path=driver_path)
search_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser.get(link)
    request_link = browser.find_element_by_link_text(search_text)
    request_link.click()
    first_name = browser.find_element_by_name('first_name')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys('Petrov')
    city = browser.find_element_by_css_selector('.city')
    city.send_keys('Smolensk')
    country = browser.find_element_by_css_selector('#country')
    country.send_keys('Russia')
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

