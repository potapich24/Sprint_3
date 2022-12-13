from locators import LocatorsForSectionConstructor

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_section_constructor():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

    #Кликаем на раздел "Начинки"
    driver.find_element(*LocatorsForSectionConstructor.TAB_FILLINGS).click()

    #Проверям, что раздел "Начинки" открылся
    assert driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_FILLINGS).text == 'Начинки'
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

    #Кликаем на раздел "Соусы"
    driver.find_element(*LocatorsForSectionConstructor.TAB_SAUCES).click()

    #Кликаем на раздел "Булки"
    driver.find_element(*LocatorsForSectionConstructor.TAB_ROLLS).click()

    #Проверяем, что раздел "Булки" открылся
    assert driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_ROLLS).text == 'Булки'
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((LocatorsForSectionConstructor.PRELOADING)))

    #Кликаем на раздел "Соусы"
    driver.find_element(*LocatorsForSectionConstructor.TAB_SAUCES).click()

    #Проверяем, что раздел "Соусы" открылся
    assert driver.find_element(*LocatorsForSectionConstructor.SELECTED_TAB_SAUCES).text == 'Соусы'

    driver.quit()

test_section_constructor()