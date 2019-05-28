import allure
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.betslip_fragment import BetslipFragment


class HomePage(BasePage):
    _all_unselected_markets = (By.CSS_SELECTOR, 'span[class$=ng-star-inserted][class^=ng-trigger]')

    @allure.step
    def open(self):
        super().navigate_to(super()._URL)
        return self

    @allure.step
    def add_ticket_from_soon(self):
        super().get_element(self._all_unselected_markets).click()
        return BetslipFragment(self._driver)

    @allure.step
    def login(self, user):
        # click login button
        # enter login
        # enter password
        # click button
        super()
        pass

