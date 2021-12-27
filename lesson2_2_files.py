import os
import time

from selenium import webdriver

my_path = os.getenv('D_PATH')
special_path = True
link ='http://suninjuly.github.io/file_input.html'
filename = 'test.txt'
if special_path:
    browser = webdriver.Chrome(executable_path=my_path)
else:
    browser = webdriver.Chrome()
try:
    browser.get(link)
    path = os.path.abspath(os.path.dirname(__file__))
    required_fields = browser.find_elements_by_css_selector(".form-control")
    for field in required_fields:
        field.send_keys('test')
    browser.find_element_by_css_selector("#file").send_keys(os.path.join(path, filename))
    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(15)
    browser.quit()
    
