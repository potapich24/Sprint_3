from locators import LocatorsForLogOutOfYourAccount
from locators import LocatorsForRegistration
from locators import LocatorsForEntrance

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_log_out_of_your_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

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

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForLogOutOfYourAccount.BUTTON_EXIT)))

    #Выход кликом по "Выход" из личного кабинета
    driver.find_element(*LocatorsForLogOutOfYourAccount.BUTTON_EXIT).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForRegistration.HEADING_ENTRANCE)))

    #Проверяем, что выход осуществлен
    assert driver.find_element(*LocatorsForRegistration.HEADING_ENTRANCE).is_displayed()
    driver.quit()

