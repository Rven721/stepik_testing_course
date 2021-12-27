import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

my_path = os.getenv('D_PATH')
link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome(executable_path=my_path)
browser.implicitly_wait(5)
try:
    browser.get(link)
    b_button = browser.find_element(By.ID, 'book')      
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    b_button.click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    my_answer = calc(int(x))
    browser.find_element(By.ID, 'answer').send_keys(my_answer)
    browser.find_element(By.ID, 'solve').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text)
finally:
    time.sleep(15)
    browser.quit()

