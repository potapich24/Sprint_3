from locators import LocatorsForSectionConstructor

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTabs:
    def test_section_constructor_fillings(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(self.driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

        #Кликаем на раздел "Начинки"
        self.driver.find_element(*LocatorsForSectionConstructor.TAB_FILLINGS).click()

        #Проверям, что раздел "Начинки" открылся
        assert self.driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_FILLINGS).text == 'Начинки'

        self.driver.quit()

    def test_section_constructor_rolls(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(self.driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

        #Кликаем на раздел "Соусы"
        self.driver.find_element(*LocatorsForSectionConstructor.TAB_SAUCES).click()

        #Кликаем на раздел "Булки"
        self.driver.find_element(*LocatorsForSectionConstructor.TAB_ROLLS).click()

        #Проверяем, что раздел "Булки" открылся
        assert self.driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_ROLLS).text == 'Булки'

        self.driver.quit()

    def test_section_constructor_sauces(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(self.driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

        #Кликаем на раздел "Соусы"
        self.driver.find_element(*LocatorsForSectionConstructor.TAB_SAUCES).click()

        #Проверяем, что раздел "Соусы" открылся
        assert self.driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_SAUCES).text == 'Соусы'

        self.driver.quit()

