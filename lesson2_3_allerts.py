import os
import time
import math

from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

my_path = os.getenv('D_PATH')
special_path = True
link = 'http://suninjuly.github.io/alert_accept.html'

if special_path:
    browser = webdriver.Chrome(executable_path=my_path)
else:
    browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_css_selector('button').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_css_selector('#input_value').text
    my_answer = calc(int(x))
    browser.find_element_by_css_selector('#answer').send_keys(my_answer)
    browser.find_element_by_css_selector('button').click()
finally:
    time.sleep(25)
    browser.quit()

