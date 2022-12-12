import random

from sprint_3.locators import LocatorsForRegistration

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Нажимаем на кнопку "Войти в аккаунт"
driver.find_element(By.CSS_SELECTOR, ".button_button_size_large__G21Vg").click()
#Нажимаем на "Зарегистрироваться"
driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

#Генерируем логин
new_login = f"mihailandreev{random.randint(0, 999)}@yandex.ru"

#Заполняем поле "Имя"
driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default']").send_keys(("Mihail"))

#Проверяем, что поле "Имя" не пустое
assert driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default']").get_attribute('value') == 'Mihail'

#Вводим логин в поле "Логин"
driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(new_login)

#Проверяем, что в веденном значении поля "Логин" есть '@yandex.ru'
assert '@yandex.ru' in driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").get_attribute('value')

#Заполняем поле "Пароль"
driver.find_element(By.XPATH, ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']").send_keys("mihail55")

#Проверяем, что длина пароля больше или ровна 6
assert len(driver.find_element(By.XPATH, ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']").get_attribute('value'))>=6

#Нажимаем кнопку "Зарегистрироваться"
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

#Проверяем, что регистарация прошла успешно и на отркывшейся странице есть элемент с надписью "Вход"
assert driver.find_element(By.XPATH, ".//h2[text()='Вход']").text == 'Вход'
driver.quit()

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Входим в аккаунт
driver.find_element(By.CSS_SELECTOR, ".button_button_size_large__G21Vg").click()
#Нажимаем на кнопку "Зарегистрироваться"
driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

#Заполняем поле "Пароль". Длина меньше 6
driver.find_element(By.XPATH, ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']").send_keys("miha")

#Нажимаем кнопку "Зарегистрироваться"
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

#Проверяем, что всплывает ошибка "Некорректный пароль", если ввести пароль менее 6 символов
assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").text == 'Некорректный пароль'
assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").is_displayed()
driver.quit()