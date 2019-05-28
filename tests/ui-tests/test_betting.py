import pytest
import time
import allure
from pages.home_page import HomePage
from pages.header_fragment import HeaderFragment
# from test-data.users import Users

class TestBetting:


    @allure.title('Unlogged user tries make bet')
    @pytest.mark.test
    def test_auth_warning(self, driver):
        home_page = HomePage(driver).open()
        betslip = home_page.add_ticket_from_soon()
        betslip.place_bet()
        assert 'register' in betslip.get_text_auth_warning()


    @allure.title('Button "Join Us" in auth warning message open registr page')
    def test_auth_warning_open_registration_page(self, driver):
        home_page = HomePage(driver).open()
        betslip = home_page.make_valid_bets(1)
        register = betslip.click_join_us_auth_warning()
        assert '/register' in register.get_url()


    @pytest.mark.skip(reason="Test Not Ready.")
    @allure.title('Double click on the button "Make A Bet" does not make a two exemplar bet')
    def test_double_click_make_one_bet(self, driver):
        user = {'email': 'test1@local.com', 'pass': 'qweasd'}
        home_page = HeaderFragment(driver).login(user)
        betslip = home_page.add_ticket_from_soon()
        betslip.set_all_amounts('0.001')
        betslip.place_bet_double_click()
        account_history_page = betslip.click_popup_account_history()
        all_bet_history = account_history_page.get_all_history()
        assert all_bet_history[2].text[1:] != all_bet_history[3].text[1:]


    @allure.title('An animation of changing balance after make bet')
    def test_change_balance_after_bet(self, driver):
        user = {'email': 'test1@local.com', 'pass': 'qweasd'}
        header = HeaderFragment(driver)
        home_page = header.login(user)
        balance_before = header.get_balance_float()
        print (balance_before)
        home_page.make_valid_bets(1)
        print (header.get_balance_float())
        time.sleep(2)
        assert balance_before != header.get_balance_float()


    @allure.title('Place more than one bet at a time')
    def test_place_5_bet_one_time(self, driver):
        count = 5
        user = {'email': 'test1@local.com', 'pass': 'qweasd'}
        header = HeaderFragment(driver)
        home_page = header.login(user)
        betslip = home_page.make_valid_bets(count)
        account_history_page = betslip.click_popup_account_history()
        time_bets = (account_history_page.get_all_date_time())[:count]
        time = time_bets[0]
        for each in time_bets:
            print (each.text)
            assert each.text == time.text


        
        