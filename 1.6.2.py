import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    time.sleep(3)
    link.click()

    input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(1) > input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(2) > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, '#submit_button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла