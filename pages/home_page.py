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
    def add_tickets_from_soon(self, count):
        markets = super().get_elements(self._all_unselected_markets)[:count]
        for each in markets:
            each.click()
        return BetslipFragment(self._driver)
            

    @allure.step
    def make_valid_bets(self, count):
        betslip = self.add_tickets_from_soon(count)
        betslip.set_all_amounts('0.001')
        betslip.place_bet()
        assert betslip.is_bet_accepted()
        return BetslipFragment(self._driver)


