import os
from selenium import webdriver
import time

driver_path = os.getenv('D_PATH')
link = 'http://suninjuly.github.io/huge_form.html'

browser = webdriver.Chrome(executable_path=driver_path)
browser.get(link)
fields = browser.find_elements_by_tag_name('input')
for field in fields:
    field.send_keys('yes')
button = browser.find_element_by_css_selector('.btn')
button.click()
time.sleep(15)
browser.quit()

