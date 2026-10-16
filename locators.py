from selenium.webdriver.common.by import By


class Locators:
    # Шапка сайта
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")  # кнопка «Вход и регистрация»
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")  # кнопка «Разместить объявление»
    AVATAR = (By.CLASS_NAME, "circleSmall")  # аватар пользователя
    USER_NAME = (By.XPATH, "//h3[contains(@class, 'profileText')]")  # имя пользователя
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # кнопка «Выйти»

    # Формы входа и регистрации
    MODAL_TITLE = (By.XPATH, "//form//h1")  # заголовок модального окна
    EMAIL_INPUT = (By.NAME, "email")  # поле Email
    PASSWORD_INPUT = (By.NAME, "password")  # поле «Пароль»
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")  # поле «Повторите пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка «Войти»
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")  # кнопка «Нет аккаунта»
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")  # кнопка «Создать аккаунт»

    # Рамки полей (при ошибке у них появляется класс input_inputError)
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']/..")  # рамка поля Email
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']/..")  # рамка поля «Пароль»
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@name='submitPassword']/..")  # рамка поля «Повторите пароль»
    EMAIL_ERROR_TEXT = (By.XPATH, "//span[text()='Ошибка']")  # сообщение «Ошибка» под Email

    # Форма создания объявления
    AD_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название']")  # поле «Название»
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")  # поле «Описание товара»
    AD_PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']")  # поле «Стоимость»
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/../button")  # стрелка dropdown «Категория»
    CATEGORY_BOOKS = (By.XPATH, "//span[text()='Книги']")  # категория «Книги»
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/../button")  # стрелка dropdown «Город»
    CITY_KAZAN = (By.XPATH, "//span[text()='Казань']")  # город «Казань»
    CONDITION_USED_RADIO = (By.XPATH, "//input[@value='Б/У']/following-sibling::div")  # radiobutton «Б/У»
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")  # кнопка «Опубликовать»

    # Профиль: объявление с заданным названием в блоке «Мои объявления»
    @staticmethod
    def my_ad_title(ad_name):
        return By.XPATH, f"//h1[text()='Мои объявления']/..//div[@class='about']/h2[text()='{ad_name}']"
