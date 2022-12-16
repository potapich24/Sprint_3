from selenium.webdriver.common.by import By
class LocatorsForRegistration:
    BUTTON_SIGN_IN_TO_ACCOUNT = By.CSS_SELECTOR, ".button_button_size_large__G21Vg" #Кнопка "Войти в аккаунт"
    BUTTON_REGISTRATION = By.XPATH, ".//a[text()='Зарегистрироваться']" #Кнопка "Зарегистрироваться"
    FIELD_NAME = By.XPATH, ".//label[text()='Имя']/following::input" #Поле "Имя"
    FIELD_LOGIN = By.XPATH, ".//label[text()='Email']/following::input" #Поле "Логин"
    FIELD_PASSWORD = By.XPATH, ".//label[text()='Пароль']/following::input" #Поле "Пароль"
    BUTTON_REGISTER = By.XPATH, ".//button[text()='Зарегистрироваться']" #Кнопка "Зарегестрироваться"
    HEADING_ENTRANCE = By.XPATH, ".//h2[text()='Вход']" #Заголовок "Вход" на странице "Вход"
    MISTAKE_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']" #Всплывающаю ошибка при вводе не валидного пароля

class LocatorsForEntrance:
    FIELD_EMAIL = By.NAME, "name" #Поле Email
    FIELD_PASSWORD =  By.NAME, "Пароль" #Поле Пароль"
    BUTTON_ENTRANCE = By.XPATH, ".//button[text()='Войти']" #Кнопка "Войти"
    HEADING_ASSEMBLE_THE_BURGER = By.XPATH, ".//h1[text()='Соберите бургер']" #Заголовок "Соберите бургер"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']" #Кнопка "Личный кабинет"
    BUTTON_ENTRANCE_CLASS = By.CLASS_NAME, "Auth_link__1fOlj" #Кнопка "Войти"
    THE_INSCRIPTION_RESTORE_PASSWORD = By.XPATH, ".//a[text()='Восстановить пароль']" #Кликабельная надпись "Восстановить пароль"

class LocatorsForLogOutOfYourAccount:
    BUTTON_EXIT = By.XPATH, ".//button[text()='Выход']" #Кнопка "Выход"

class LocatorsForSectionConstructor:
    PRELOADING = By.XPATH, ".//img[@alt='loading animation']" #Плейоудер при загрузке страницы
    TAB_FILLINGS = By.XPATH, ".//span[text()='Начинки']/parent::div" # Вкладка "Начинки"
    SELECTED_TAB = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #Выбранная вкладка "Начинки"
    TAB_SAUCES = By.XPATH, ".//span[text()='Соусы']/parent::div" #Вкладка "Соусы"
    TAB_ROLLS = By.XPATH, ".//span[text()='Булки']/parent::div" #Вкладка "Булки"

class LocatrsForSwitchingFromYourAccountToTheConstructor:
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']" #Кнопка "Конструктор"
    LOGO = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']" #Логотип

class LocatrsForTransferToYouPersonalAccount:
    HEADING_PROFILE = By.XPATH, ".//a[text()='Профиль']" #Заголовок "Профиль"