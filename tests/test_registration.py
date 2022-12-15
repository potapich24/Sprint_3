import random

from locators import LocatorsForRegistration

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        # Генерируем логин
        new_login = f"mihailandreev{random.randint(0, 999)}@yandex.ru"

        # Заполняем поле "Имя"
        self.driver.find_element(*LocatorsForRegistration.FIELD_NAME).send_keys(("Mihail"))

        # Вводим логин в поле "Логин"
        self.driver.find_element(*LocatorsForRegistration.FIELD_LOGIN).send_keys(new_login)

        # Заполняем поле "Пароль"
        self.driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).send_keys("mihail55")

        # Нажимаем кнопку "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTER).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsForRegistration.HEADING_ENTRANCE)))

        # Проверяем, что регистарация прошла успешно и на отркывшейся странице есть элемент с надписью "Вход"
        assert self.driver.find_element(*LocatorsForRegistration.HEADING_ENTRANCE).text == 'Вход'
        self.driver.quit()

    def test_check_field_name_not_empty(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        # Заполняем поле "Имя"
        self.driver.find_element(*LocatorsForRegistration.FIELD_NAME).send_keys(("Mihail"))

        # Проверяем, что поле "Имя" не пустое
        assert self.driver.find_element(*LocatorsForRegistration.FIELD_NAME).get_attribute('value') == 'Mihail'

        self.driver.quit()

    def test_check_field_login_format(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        new_login = f"mihailandreev{random.randint(0, 999)}@yandex.ru"

        #Вводим логин в поле "Логин"
        self.driver.find_element(*LocatorsForRegistration.FIELD_LOGIN).send_keys(new_login)

        #Проверяем, что в веденном значении поля "Логин" есть '@yandex.ru'
        assert '@yandex.ru' in self.driver.find_element(*LocatorsForRegistration.FIELD_LOGIN).get_attribute('value')

        self.driver.quit()
    def test_check_field_value_length(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        #Заполняем поле "Пароль"
        self.driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).send_keys("mihail55")

        #Проверяем, что длина пароля больше или ровна 6
        assert len(self.driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).get_attribute('value'))>=6

        self.driver.quit()

    def test_check_error(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Нажимаем на кнопку "Войти в аккаунт"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_SIGN_IN_TO_ACCOUNT).click()

        # Нажимаем на "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTRATION).click()

        #Заполняем поле "Пароль". Длина меньше 6
        self.driver.find_element(*LocatorsForRegistration.FIELD_PASSWORD).send_keys("miha")

        #Нажимаем кнопку "Зарегистрироваться"
        self.driver.find_element(*LocatorsForRegistration.BUTTON_REGISTER).click()

        #Проверяем, что всплывает ошибка "Некорректный пароль", если ввести пароль менее 6 символов
        assert self.driver.find_element(*LocatorsForRegistration.MISTAKE_PASSWORD).text == 'Некорректный пароль'

        self.driver.quit()

