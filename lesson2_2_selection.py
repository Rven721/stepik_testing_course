import os
import time
import math

from selenium import webdriver

driver_path = os.getenv('D_PATH')
special_path = False 
link = "http://suninjuly.github.io/selects2.html"

if special_path:
    browser = webdriver.Chrome(executable_path=driver_path)
else:
    brower = webdriver.Chrome() 
try:
    browser.get(link)
    num1 = browser.find_element_by_css_selector("#num1").text
    num2 = browser.find_element_by_css_selector("#num2").text
    my_answer = sum(map(int, [num1, num2]))
    select = webdriver.support.ui.Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(my_answer))
    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(10)
    browser.quit()
