from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[@alt='loading animation']")))

#Кликаем на раздел "Начинки"
driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::div").click()

#Проверям, что раздел "Начинки" открылся
assert driver.find_element(By.XPATH, ".//div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Начинки'
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[@alt='loading animation']")))

#Кликаем на раздел "Соусы"
driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").click()

#Кликаем на раздел "Булки"
driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").click()

#Проверяем, что раздел "Булки" открылся
assert driver.find_element(By.XPATH, ".//div[1][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Булки'
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

WebDriverWait(driver, 6).until_not(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[@alt='loading animation']")))

#Кликаем на раздел "Соусы"
driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").click()

#Проверяем, что раздел "Соусы" открылся
assert driver.find_element(By.XPATH, ".//div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Соусы'

driver.quit()