from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Нажимаем на кнопку "Войти в аккаунт"
driver.find_element(By.CSS_SELECTOR, ".button_button_size_large__G21Vg").click()

#Вводим Email
driver.find_element(By.NAME, "name").send_keys('mihailandreev5@yandex.ru')
#Вводим пароль
driver.find_element(By.NAME, "Пароль").send_keys('mihail55')
#Нажимаем войти
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))

#Входим в личный кабинет
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))

#Выход кликом по "Выход" из личного кабинета
driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

#Проверяем, что выход осуществлен
assert driver.find_element(By.XPATH, ".//h2[text()='Вход']").text == 'Вход'
assert driver.find_element(By.XPATH, ".//h2[text()='Вход']").is_displayed()
driver.quit()