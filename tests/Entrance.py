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

#Проверяем, что вход через "Войти в аккаунт" осуществлен
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']").text == 'Соберите бургер'

driver.quit()

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Входим в личный кабинет
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

#Вводим Email
driver.find_element(By.NAME, "name").send_keys('mihailandreev5@yandex.ru')
#Вводим пароль
driver.find_element(By.NAME, "Пароль").send_keys('mihail55')
#Нажимаем войти
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

#Проверяем, что вход через "Личный Кабинет" осуществлен
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']").text == 'Соберите бургер'

driver.quit()

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Нажимаем на кнопку "Войти в аккаунт"
driver.find_element(By.CSS_SELECTOR, ".button_button_size_large__G21Vg").click()

#Нажимаем на "Зарегистрироваться"
driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

#Нажимаем на "Войти"
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

#Вводим Email
driver.find_element(By.NAME, "name").send_keys('mihailandreev5@yandex.ru')
#Вводим пароль
driver.find_element(By.NAME, "Пароль").send_keys('mihail55')
#Нажимаем войти
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

#Проверяем, что вход через форму регистраци осуществлен
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']").text == 'Соберите бургер'

driver.quit()

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

#Входим в личный кабинет
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

#Нажимаем на "Восстановить пароль"
driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()

#Нажимаем "Войти"
driver.find_element(By.XPATH, ".//a[text()='Войти']").click()

#Вводим Email
driver.find_element(By.NAME, "name").send_keys('mihailandreev5@yandex.ru')
#Вводим пароль
driver.find_element(By.NAME, "Пароль").send_keys('mihail55')
#Нажимаем войти
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

#Проверяем, что вход через форму восстановления пароля осуществлен
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']").text == 'Соберите бургер'

driver.quit()