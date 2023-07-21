import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    print(str(math.log(abs(12 * math.sin(int(x))))))

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    button.click()

    button = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    button.click()


finally:
    time.sleep(5)
    browser.quit()
