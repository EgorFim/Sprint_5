from selenium.webdriver.common.by import By


class TestLocators:
    NAME_INPUT_FIELD = By.XPATH,'//label[ text()="Имя" ]/parent::div/input'
    #поле ввода имени при регистрации
    EMAIL_INPUT_FIELD = By.XPATH, '//label[ text()="Email" ]/parent::div/input'
    #поле ввода почты при регистрации
    PASSWORD_INPUT_FIELD = By.XPATH, '//label[ text()="Пароль" ]/parent::div/input'
    #поле ввода пароля при регистрации
    VOITY_BUTTON = By.XPATH,'.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    #кнопка "Войти в аккаунт" на главной странице
    REGISTER_BUTTON_1 = By.XPATH, './/a[@class = "Auth_link__1fOlj"]'
    #кнопка "Зарегистрироваться" на окне авторизации
    REGISTER_BUTTON_FINAL = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    #кнопка "Зарегистрироваться" на окне регистрации
    EMAIL_ADD = By.XPATH, './/input[@class="text input__textfield text_type_main-default"]'
    #поле email в окне авторизации
    PASSWORD_ADD = By.XPATH, './/input[@type="password"]'
    #поле password в окне авторизации
    VOITY_BUTTON_AFTER_ADD = By.XPATH, './/button[text()="Войти"]'
    #кнопка "Войти" в окне авторизации
    PROVERKA_USPESHNOGO_VHODA = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    #поиск кнопки "Оформить заказ" на главной
    OZHIDANIE_POSLE_ZAPOLNENIYA_REGISTRACII = By.XPATH, './/h2[text()="Вход"]'
    #ожидание загрузки после регистрации
    NEVERNIY_PAROL = By.XPATH,'.//p[@class="input__error text_type_main-default"]'
    #проверка что пароль введен не верно
    KNOPKA_LICHNYI_KABINET = By.XPATH, './/*[text()="Личный Кабинет"]'
    #кнопка "Личный кабинет" на главной
    VOITY_IZ_OKNA_REGISTRACII = By.XPATH, './/*[text()="Войти"]'
    #кнопка "Войти" в окне ренистрации
    KNOPKA_VOSSTANOVIT_PAROL = By.XPATH, './/*[text()="Восстановить пароль"]'
    #кнопка "Восстановить" в окне авторизации
    V_LICHNOM_KABINETE = By.XPATH, './/*[text()="В этом разделе вы можете изменить свои персональные данные"]'
    #поиск элемента с текстом "В этом разделе вы можете изменить свои персональные данные"
    ZAGRUZKA_GLAVNOI = By.XPATH, './/*[@class="AppHeader_header__logo__2D0X2"]'
    #поиск хедера на главной
    KNOPKA_KONSTRUKTOR = By.XPATH, './/*[text()="Конструктор"]'
    #поиск кнопки "Конструктор"
    KONSTRUKTOR_PROVERKA = By.XPATH, './/*[text()="Соберите бургер"]'
    #поиск текста "Соберите бургер"
    KNOPKA_STELLAR = By.XPATH, './/*[@class="AppHeader_header__logo__2D0X2"]'
    #кнопка Stellar Burger
    KNOPKA_VYHOD = By.XPATH, './/button[text()="Выход"]'
    #кнопка "Выход"
    KNOPKA_SOUSY = By.XPATH, './/*[text()="Соусы"]'
    #кнопка "Соусы"
    KNOPKA_BULKI = By.XPATH, './/*[text()="Булки"]'
    #кнопка "Булки"
    KNOPKA_NACHINKI = By.XPATH, './/*[text()="Начинки"]'
    #кнопка "Начинки"
    PROVERKA_VKLADKA_SOUSY = By.XPATH, './/*[text()="Соус Spicy-X"]'
    #поиск названия соуса
    PROVERKA_VKLADKA_BULKI = By.XPATH, './/*[text()="Флюоресцентная булка R2-D3"]'
    #поиск названия булки
    PROVERKA_VKLADKA_NACHINKI = By.XPATH, './/*[text()="Мясо бессмертных моллюсков Protostomia"]'
    #поиск названия начинки
