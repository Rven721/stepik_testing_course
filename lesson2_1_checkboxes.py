import os
import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver_path = os.getenv('D_PATH')
special_driver = True
link = 'http://suninjuly.github.io/math.html'

if special_driver:
    browser = webdriver.Chrome(executable_path=driver_path)
else:
    browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    my_answer = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(my_answer)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    browser.find_element_by_css_selector("button").click()

finally:
    time.sleep(10)
    browser.quit()

