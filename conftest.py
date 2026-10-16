import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import URL
from helpers import generate_email
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def new_user_driver(driver):
    # Заранее создаём нового пользователя без объявлений, после регистрации он сразу авторизован
    driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REPEAT_PASSWORD_INPUT))
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))
    return driver
