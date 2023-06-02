from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    first_button = browser.find_element(By.CLASS_NAME, 'btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value')
    y = int(x.text)
    answer = browser.find_element(By.ID, 'answer').send_keys(calc(y))

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(50)

    a = browser.switch_to.alert.text
    print(a)


finally:
    time.sleep(5)
    browser.quit()