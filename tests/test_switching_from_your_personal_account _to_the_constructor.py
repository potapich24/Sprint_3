from locators import LocatrsForSwitchingFromYourAccountToTheConstructor
from locators import LocatorsForRegistration
from locators import LocatorsForEntrance

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSwitchingFromYourPersonalAccountToTheConstructor:
    def test_switching_the_constructor_button_to_the_constructor(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        # Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        # Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

        # Входим в личный кабинет
        self.driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

        # Проверяем переход в конструктор по кнопке "Конструктор"
        self.driver.find_element(*LocatrsForSwitchingFromYourAccountToTheConstructor.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()

    def test_switching_logo_to_the_constructor(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Вводим Email
        self.driver.find_element(*LocatorsForEntrance.FIELD_EMAIL).send_keys('mihailandreev5@yandex.ru')
        # Вводим пароль
        self.driver.find_element(*LocatorsForEntrance.FIELD_PASSWORD).send_keys('mihail55')
        # Нажимаем войти
        self.driver.find_element(*LocatorsForEntrance.BUTTON_ENTRANCE).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

        # Входим в личный кабинет
        self.driver.find_element(*LocatorsForEntrance.BUTTON_PERSONAL_ACCOUNT).click()

        # Проверяем переход в конструктор по логотипу
        self.driver.find_element(*LocatrsForSwitchingFromYourAccountToTheConstructor.LOGO).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER)))

        assert self.driver.find_element(*LocatorsForEntrance.HEADING_ASSEMBLE_THE_BURGER).is_displayed()
        self.driver.quit()
