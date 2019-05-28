import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.register_page import RegisterPage
from pages.account_history_page import AccountHistoryPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class BetslipFragment(BasePage):
    _place_bet_button = (By.CSS_SELECTOR, 'button.bet-button')
    _auth_warning = (By.CSS_SELECTOR, 'div.auth')
    _join_us_button_auth_warning = (By.CSS_SELECTOR, '.bill-button.mt-3')
    _popup_accepted_history_button = (By.CSS_SELECTOR, '.accepted_button.bet-button')
    _all_amounts = (By.CSS_SELECTOR, 'input.bet-input')


    @allure.step
    def set_all_amounts(self, amount):
        for amount_input in super().get_elements(self._all_amounts):
            amount_input.send_keys(Keys.BACKSPACE)
            amount_input.send_keys(amount)


    @allure.step
    def place_bet(self):
        super().get_element(self._place_bet_button).click()


    @allure.step
    def place_bet_double_click(self):
        button = super().get_element(self._place_bet_button)
        button.click()
        button.click()


    @allure.step
    def is_bet_accepted(self):
        try:
            super().get_element(self._popup_accepted_history_button)
            return True
        except NoSuchElementException:
            return False


    @allure.step
    def get_text_auth_warning(self):
        return super().get_element(self._auth_warning).text


    @allure.step
    def click_join_us_auth_warning(self):
        super().get_element(self._join_us_button_auth_warning).click()
        return RegisterPage(self._driver)


    @allure.step
    def click_popup_account_history(self):
        super().get_element(self._popup_accepted_history_button).click()
        return AccountHistoryPage(self._driver)