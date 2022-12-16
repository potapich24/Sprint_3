from selenium import webdriver

from locators import LocatorsForEntrance
from locators import LocatorsForRegistration

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_entrance_login_via_account(driver):
    #Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

    #Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    #Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    #Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    #Проверяем, что вход через "Войти в аккаунт" осуществлен
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()


def test_entrance_login_via_personal_account(driver):
    #Входим в личный кабинет
    driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

    #Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    #Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    #Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    #Проверяем, что вход через "Личный Кабинет" осуществлен
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()


def test_entrance_login_via_registration_form(driver):
    #Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

    #Нажимаем на "Зарегистрироваться"
    driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

    #Нажимаем на "Войти"
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE_CLASS).click()

    #Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    #Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    #Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    #Проверяем, что вход через форму регистраци осуществлен
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()

def test_entrance_login_via_password_recovery_form(driver):
    #Входим в личный кабинет
    driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

    #Нажимаем на "Восстановить пароль"
    driver.find_element(*LocatorsForEntrance.THE_INSCRIPTION_RESTORE_PASSWORD).click()

    #Нажимаем "Войти"
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE_CLASS).click()

    #Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    #Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    #Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    #Проверяем, что вход через форму восстановления пароля осуществлен
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()


