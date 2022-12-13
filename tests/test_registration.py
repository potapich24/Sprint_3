import random

from locators import LocatorsForRegistration

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    #Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()
    #Нажимаем на "Зарегистрироваться"
    driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

    #Генерируем логин
    new_login = f"mihailandreev{random.randint(0, 999)}@yandex.ru"

    #Заполняем поле "Имя"
    driver.find_element(*LocatorsForRegistration.FIELD_NAME).send_keys(("Mihail"))

    #Проверяем, что поле "Имя" не пустое
    assert driver.find_element(*LocatorsForRegistration.FIELD_NAME).get_attribute('value') == 'Mihail'

    #Вводим логин в поле "Логин"
    driver.find_element(*LocatorsForRegistration.FIELD_LOGIN).send_keys(new_login)

    #Проверяем, что в веденном значении поля "Логин" есть '@yandex.ru'
    assert '@yandex.ru' in driver.find_element(*LocatorsForRegistration.FIELD_LOGIN).get_attribute('value')

    #Заполняем поле "Пароль"
    driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).send_keys("mihail55")

    #Проверяем, что длина пароля больше или ровна 6
    assert len(driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).get_attribute('value'))>=6

    #Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*LocatorsForRegistration.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForRegistration.HEADING_ENTRANCE)))

    #Проверяем, что регистарация прошла успешно и на отркывшейся странице есть элемент с надписью "Вход"
    assert driver.find_element(*LocatorsForRegistration.HEADING_ENTRANCE).text == 'Вход'
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    #Входим в аккаунт
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()
    #Нажимаем на кнопку "Зарегистрироваться"
    driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

    #Заполняем поле "Пароль". Длина меньше 6
    driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).send_keys("miha")

    #Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*LocatorsForRegistration.BUTTON_REGISTER).click()

    #Проверяем, что всплывает ошибка "Некорректный пароль", если ввести пароль менее 6 символов
    assert driver.find_element(*LocatorsForRegistration.MISTAKE_PASSWORD).text == 'Некорректный пароль'
    assert driver.find_element(*LocatorsForRegistration.MISTAKE_PASSWORD).is_displayed()
    driver.quit()

test_registration()

