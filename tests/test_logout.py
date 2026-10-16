from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import EMAIL, PASSWORD
from locators import Locators


class TestLogout:

    def test_logout_user(self, driver):
        # Авторизация под заранее созданным пользователем
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_AND_REGISTRATION_BUTTON))

        assert driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).is_displayed()
        assert len(driver.find_elements(*Locators.AVATAR)) == 0
