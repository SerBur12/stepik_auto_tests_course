from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, 'firstname')
    first._execute()

    last = browser.find_element(By.NAME, 'lastname')
    last.send_keys('Last name')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Email')

    load_file = browser.find_element(By.CSS_SELECTOR, '[type=file]')
    load_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()
