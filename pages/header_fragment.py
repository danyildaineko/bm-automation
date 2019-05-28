import allure
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException
import time

class HeaderFragment(BasePage):   
    _open_login_form = (By.CLASS_NAME, 'btn-login')
    _email_input = (By.ID, 'email')
    _login_input = (By.ID, 'pass')
    _login_button = (By.CSS_SELECTOR, 'div.login-button > button.btn-submit') 
    _buy_token_url = (By.PARTIAL_LINK_TEXT, 'Вuу Тоkеns')
    _balance = (By.CSS_SELECTOR, 'div.currency span.color-text')

    @allure.step
    def login(self, user):
        super().navigate_to(super()._URL)
        super().get_element(self._open_login_form).click()
        super().get_element(self._email_input).send_keys(user['email'])
        super().get_element(self._login_input).send_keys(user['pass'])
        super().get_element(self._login_button).click()
        if super().get_element(self._buy_token_url):
            return HomePage(self._driver)
        else:
            assert False, 'User is not logged.'

    def get_balance_float(self):
        return float(super().get_element(self._balance).text.split(' ')[0])
