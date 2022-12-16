from locators import LocatrsForSwitchingFromYourAccountToTheConstructor
from locators import LocatorsForRegistration
from locators import LocatorsForEntrance

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_switching_the_constructor_button_to_the_constructor(driver):
    #Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

    #Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    #Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    #Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

    #Входим в личный кабинет
    driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

    # Проверяем переход в конструктор по кнопке "Конструктор"
    driver.find_element(*LocatrsForSwitchingFromYourAccountToTheConstructor.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()


def test_switching_logo_to_the_constructor(driver):
    #Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

    # Вводим Email
    driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
    # Вводим пароль
    driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
    # Нажимаем войти
    driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

    #Входим в личный кабинет
    driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

    # Проверяем переход в конструктор по логотипу
    driver.find_element(*LocatrsForSwitchingFromYourAccountToTheConstructor.LOGO).click()
    WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

    assert driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()

