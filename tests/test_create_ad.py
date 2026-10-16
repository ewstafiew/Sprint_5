from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import URL
from helpers import generate_ad_name
from locators import Locators


class TestCreateAd:

    def test_create_ad_unauthorized_user(self, driver):
        driver.find_element(*Locators.PLACE_AD_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.MODAL_TITLE))

        assert driver.find_element(*Locators.MODAL_TITLE).text == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_authorized_user(self, new_user_driver):
        driver = new_user_driver

        # Заполняем форму объявления
        ad_name = generate_ad_name()
        driver.find_element(*Locators.PLACE_AD_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AD_NAME_INPUT))
        driver.find_element(*Locators.AD_NAME_INPUT).send_keys(ad_name)
        driver.find_element(*Locators.AD_DESCRIPTION_INPUT).send_keys("Хорошая книга")
        driver.find_element(*Locators.AD_PRICE_INPUT).send_keys("500")

        driver.find_element(*Locators.CATEGORY_DROPDOWN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CATEGORY_BOOKS)).click()

        driver.find_element(*Locators.CITY_DROPDOWN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CITY_KAZAN)).click()

        driver.find_element(*Locators.CONDITION_USED_RADIO).click()
        driver.find_element(*Locators.PUBLISH_BUTTON).click()

        # После публикации открывается главная страница, переходим в профиль
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(URL))
        driver.find_element(*Locators.AVATAR).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.my_ad_title(ad_name)))

        assert driver.find_element(*Locators.my_ad_title(ad_name)).text == ad_name
