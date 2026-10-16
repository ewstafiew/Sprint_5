from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import EMAIL, PASSWORD
from locators import Locators


class TestLogin:

    def test_login_user(self, driver):
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))

        assert driver.find_element(*Locators.AVATAR).is_displayed()
        assert driver.find_element(*Locators.USER_NAME).text == "User."
