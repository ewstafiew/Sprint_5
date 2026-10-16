from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import EMAIL, PASSWORD
from helpers import generate_email
from locators import Locators


class TestRegistration:

    def test_registration_new_user(self, driver):
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))

        assert driver.find_element(*Locators.AVATAR).is_displayed()
        assert driver.find_element(*Locators.USER_NAME).text == "User."

    def test_registration_invalid_email(self, driver):
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("evstafev_39gmail.com")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_ERROR_TEXT))

        assert "input_inputError" in driver.find_element(*Locators.EMAIL_FIELD).get_attribute("class")
        assert "input_inputError" in driver.find_element(*Locators.PASSWORD_FIELD).get_attribute("class")
        assert "input_inputError" in driver.find_element(*Locators.REPEAT_PASSWORD_FIELD).get_attribute("class")
        assert driver.find_element(*Locators.EMAIL_ERROR_TEXT).text == "Ошибка"

    def test_registration_existing_user(self, driver):
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REPEAT_PASSWORD_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_ERROR_TEXT))

        assert "input_inputError" in driver.find_element(*Locators.EMAIL_FIELD).get_attribute("class")
        assert "input_inputError" in driver.find_element(*Locators.PASSWORD_FIELD).get_attribute("class")
        assert "input_inputError" in driver.find_element(*Locators.REPEAT_PASSWORD_FIELD).get_attribute("class")
        assert driver.find_element(*Locators.EMAIL_ERROR_TEXT).text == "Ошибка"
