import os
import math
import time

from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

my_path = os.getenv('D_PATH')
special_path = True
link = 'http://SunInJuly.github.io/execute_script.html'

if special_path:
    browser = webdriver.Chrome(executable_path=my_path)
else:
    browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    my_answer = calc(int(x))
    browser.find_element_by_css_selector("#answer").send_keys(my_answer)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    robocheck = browser.find_element_by_css_selector("[value='robots']")
    button = browser.find_element_by_css_selector("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robocheck.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
