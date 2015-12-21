from selenium.webdriver.common.by import By
from pypom import Page
from .key_press_page import KeyPressPage

class MainPage(Page):

    _url = '{base_url}'
    _loc_key_press = (By.XPATH, "//*[@href='/key_presses']")

    def open_key_presses_page(self):
        #self.find_element(self._loc_key_press).click()
        self.selenium.find_element("xpath", "//*[@href='/key_presses']")
        key_press_page = KeyPressPage(self.base_url, self.selenium)
        return key_press_page.open()
