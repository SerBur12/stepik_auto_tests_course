import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )

    button.click()

    x = browser.find_element(By.ID, 'input_value')
    y = int(x.text)
    answer2 = browser.find_element(By.ID, 'answer').send_keys(calc(y))

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    message = browser.find_element(By.ID, "verify_message")

    a = browser.switch_to.alert.text
    print(a)
finally:
    time.sleep(10)
    browser.quit()