import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text

    answer = str(int(x) + int(y))


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    time.sleep(5)
    browser.quit()




