from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    _URL = "http://dev.btm.idl.local"

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        # self._driver.implicitly_wait = 10

    def navigate_to(self, url):
        self._driver.get(url)

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.presence_of_element_located(locator), ' : '.join(locator))
        

    def get_elements(self, locator: tuple, timeout=5):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_all_elements_located(locator), ' : '.join(locator))
        

    def get_url(self):
        return self._driver.current_url

    def refresh(self):
        self._driver.refresh()

    # def retrying_click(self, locator:tuple, timeout=10):
    #     attempts = 0
    #     while attempts < 2:
    #         try:
    #             self.get_element(locator).click()
    #             break
    #         except StaleElementReferenceException:
    #             attempts += 1
    #             self.refresh()
    #         assert False, 'GOVNO'

            
