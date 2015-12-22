from selenium.webdriver.common.by import By
from pypom import Page


class KeyPressPage(Page):
    _url = '{base_url}/key_presses'
    _loc_page_title = (By.XPATH, "//*[@id='content']/div/h3")
    _loc_page_result = (By.XPATH, "//*[@id='result']")

    def type(self, key):
        """ key keypress to be sent """
        self.find_element(self._loc_page_title).send_keys(key)

    @property
    def result(self):
        value = self.find_element(self._loc_page_result).text
        return value
