import pytest
from selenium import webdriver
# import random
#
# @pytest.fixture()
# def creating_valid_name():
#     return {'name':'Sergey', 'email':('sergeykravchenko5_'+str(random.randint(100, 999))+'@yandex.ru'), 'password': str(random.randint(100000, 999999))}

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

# @pytest.fixture()
# def account_this_incorrected_password():
#     return {'email': 'sss@yandex.ru', 'password': str(random.randint(10000, 99999))}
#
# @pytest.fixture()
# def registered_account():
#     return {'email': 'www@ya.ru', 'password': '123456'}