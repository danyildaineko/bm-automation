import allure
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountHistoryPage(BasePage):
    _all_history = (By.CSS_SELECTOR, '.item-wrapp.ng-star-inserted')
    _all_date_time = (By.CSS_SELECTOR, 'div.col-7.col-xl-12.item-date')

    def get_all_history(self):
        return super().get_elements(self._all_history)


    def get_all_date_time(self):
        return super().get_elements(self._all_date_time)