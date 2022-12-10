Локаторы Registration:
.button_button_size_large__G21Vg #Кнопка "Войти в аккаунт"
.//a[text()='Зарегистрироваться'] #Кнопка "Зарегистрироваться"
.//input[@class='text input__textfield text_type_main-default'] #Поле "Имя"
.//fieldset[2]//input[@class='text input__textfield text_type_main-default'] #Поле "Логин"
.//fieldset[3]//input[@class='text input__textfield text_type_main-default'] #Поле "Пароль"
.//button[text()='Зарегистрироваться'] #Кнопка "Зарегестрироваться"
.//h2[text()='Вход'] #Заголовок "Вход" на странице "Вход"
.//p[text()='Некорректный пароль'] #Всплывающаю ошибка при вводе не валидного пароля

Локаторы Entrance:
By.NAME, "name" #Поле Email
By.NAME, "Пароль" #Поле Пароль"
.//button[text()='Войти'] #Кнопка "Войти"
.//h1[text()='Соберите бургер'] #Заголовок "Соберите бургер"
.//p[text()='Личный Кабинет'] #Кнопка "Личный кабинет"
By.CLASS_NAME, "Auth_link__1fOlj" #Кнопка "Войти"
.//a[text()='Восстановить пароль' #Кликабельная надпись "Восстановить пароль"

Локаторы Log_out_of_your_account:
.//button[text()='Выход'] #Кнопка "Выход"

Локаторы Section_Constructor
.//img[@alt='loading animation' #Плейоудер при загрузке страницы
.//span[text()='Начинки']/parent::div # Вкладка "Начинки"
.//div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] #Выбранная вкладка "Начинки"
.//span[text()='Соусы']/parent::div #Вкладка "Соусы"
.//span[text()='Булки']/parent::div #Вкладка "Булки"
.//div[1][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] #Выбранная вкладка "Булки"
.//div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] #Выбранная вкладка "Соусы"

Локаторы Switching_from_your_accaount_to_the_constructor
.//p[text()='Конструктор'] #Кнопка "Конструктор"
.//div[@class='AppHeader_header__logo__2D0X2'] #Логотип

Локаторы Transfer_to_you_personal_account
.//a[text()='Профиль' #Заголовок "Профиль"