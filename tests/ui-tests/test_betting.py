import pytest
import time
import allure
from pages.home_page import HomePage
# from test-data.users import Users

class TestBetting:


    @allure.title('Unlogged user tries make bet')
    def test_auth_warning(self, driver):
        home_page = HomePage(driver).open()
        betslip = home_page.add_ticket_from_soon()
        betslip.make_bet()
        assert 'register' in betslip.get_text_auth_warning()


    @allure.title('Button "Join Us" in auth warning message open registr page')
    def test_auth_warning_open_registration_page(self, driver):
        home_page = HomePage(driver).open()
        betslip = home_page.add_ticket_from_soon()
        betslip.make_bet()
        register = betslip.click_join_us_auth_warning()
        assert '/register' in register.get_url()

    @allure.title('Double click on the button "Make A Bet" does not make a two exemplar bet')
    def test_double_click_make_one_bet(self, driver):
        '''
        1. Add any ticket to betslip.
        2. Set any valid amount for bet.
        3. Make double click on button ""Place A Bet"".
        4. Close popup.
        5. Open ""Account History"" page.
        '''
        # home_page = HomePage(driver).open().login(Users.get_user('b_user1'))
        pass
