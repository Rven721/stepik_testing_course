import os
import time
from selenium import webdriver

driver_path = os.getenv('D_PATH')
link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(link)
    fields = browser.find_elements_by_tag_name('input')
    for field in fields:
        field.send_keys('yes')
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
