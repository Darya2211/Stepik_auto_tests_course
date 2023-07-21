import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(12)

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID,'book')
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    print(answer)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

#title_is Соответствует ли заголовок текущего окна или вкладки браузера указанному тексту заголовка. 
#title_contains Содержит ли заголовок текущего окна или вкладки браузера указанный текст. 
#presence_of_element_located Присутствует ли указанный элемент в DOM (объектной модели документа) текущей страницы. 
#visibility_of_element_located Виден ли указанный элемент на текущей странице. 
#visibility_of Виден ли указанный элемент на текущей странице и имеет ли он ненулевой размер. 
#presence_of_all_elements_located Присутствуют ли все элементы, соответствующие указанному локатору, в DOM текущей страницы. 
#text_to_be_present_in_element  Присутствует ли указанный текст во внутреннем HTML указанного элемента. 
#text_to_be_present_in_element_value Присутствует ли указанный текст в атрибуте value указанного элемента. 
#frame_to_be_available_and_switch_to_it Доступен ли указанный фрейм на текущей странице, и если да, то переключается на фрейм. 
#invisibility_of_element_located Не отображается ли указанный элемент на текущей странице. 
#element_to_be_clickable Виден ли указанный элемент на текущей странице и доступен ли для него щелчок. 
#staleness_of Не привязан ли указанный элемент к DOM текущей страницы. 
#element_to_be_selected Ожидает выбора элемента в DOM. 
#element_located_to_be_selected Ожидает появления элемента в DOM, а также его выбора. 
#element_selection_state_to_be Ожидает, пока элемент будет иметь определенное состояние выбора. 
#element_located_selection_state_to_be  Ожидает появления элемента в DOM и с определенным состоянием выбора.
#alert_is_present Ожидает появления предупреждения. 

#Общее
#http://chromedriver.chromium.org/getting-started﻿
#﻿https://www.guru99.com/selenium-tutorial.html — ﻿Туториал на английском, ориентирован на Java.﻿
#https://www.guru99.com/live-selenium-project.html — ﻿Можно попробовать писать автотесты для демо-сайта ﻿банка. Тоже Java.
#http://barancev.github.io/good-locators/ — что такое хорошие селекторы
#http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная? 
#Ожидания в Selenium WebDriver
#https://www.selenium.dev/documentation/webdriver/waits/﻿﻿
#https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
#https://blog.codeship.com/get-selenium-to-wait-for-page-load/
#http://barancev.github.io/slow-loading-pages/
#http://barancev.github.io/page-loading-complete/

