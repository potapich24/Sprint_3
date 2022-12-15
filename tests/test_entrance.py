from selenium import webdriver

from locators import LocatorsForEntrance
from locators import LocatorsForRegistration

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestEntrance:
    def test_entrance_login_via_account(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        #Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        #Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        #Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        #Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        #Проверяем, что вход через "Войти в аккаунт" осуществлен
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()

    def test_entrance_login_via_personal_account(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        #Входим в личный кабинет
        self.driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

        #Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        #Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        #Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        #Проверяем, что вход через "Личный Кабинет" осуществлен
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()

    def test_entrance_login_via_registration_form(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        #Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        #Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        #Нажимаем на "Войти"
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE_CLASS).click()

        #Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        #Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        #Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        #Проверяем, что вход через форму регистраци осуществлен
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()
    def test_entrance_login_via_password_recovery_form(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        #Входим в личный кабинет
        self.driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

        #Нажимаем на "Восстановить пароль"
        self.driver.find_element(*LocatorsForEntrance.THE_INSCRIPTION_RESTORE_PASSWORD).click()

        #Нажимаем "Войти"
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE_CLASS).click()

        #Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        #Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        #Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        #Проверяем, что вход через форму восстановления пароля осуществлен
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))
        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()

