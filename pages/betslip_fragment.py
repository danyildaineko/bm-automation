import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class BetslipFragment(BasePage):
    _place_bet_button = (By.CSS_SELECTOR, 'button.bet-button')
    _auth_warning = (By.CSS_SELECTOR, 'div.auth')
    _join_us_button_auth_warning = (By.CSS_SELECTOR, '.bill-button.mt-3')


    @allure.step
    def make_bet(self):
        super().get_element(self._place_bet_button).click()

    @allure.step
    def get_text_auth_warning(self):
        return super().get_element(self._auth_warning).text

    @allure.step
    def click_join_us_auth_warning(self):
        super().get_element(self._join_us_button_auth_warning).click()
        return RegisterPage(self._driver)