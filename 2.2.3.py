import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)')
    input1.send_keys("Гордон")

    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)')
    input2.send_keys("Шамуэй")

    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)')
    input2.send_keys("CatJuise@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    name_object = browser.find_element(By.ID, 'file')
    #находим элемент отвечающий за отправку файла на странице и сохраняем в обЪект
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #текущая директория вашего файла txt
    file_path = os.path.join(current_dir, 'file.txt')
    #добавляет имя файла
    name_object.send_keys(file_path)
    #это тот злополучный element, который непонятно откуда берется

    submit_button = browser.find_element(By.CSS_SELECTOR,'body > div > form > button')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()





