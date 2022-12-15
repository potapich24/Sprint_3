from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatrsForTransferToYouPersonalAccount
from locators import LocatorsForRegistration
from locators import LocatorsForEntrance

def test_transfer_to_you_personal_account():
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

    #Проверям, что открылась страница "Личный кабинет"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LocatrsForTransferToYouPersonalAccount.HEADING_PROFILE)))
    assert driver.find_element(*LocatrsForTransferToYouPersonalAccount.HEADING_PROFILE).is_displayed()
    driver.quit()

