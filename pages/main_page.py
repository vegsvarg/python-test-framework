from selenium.webdriver.common.by import By
from pypom import Page
from .key_press_page import KeyPressPage
from .drag_and_drop_page import DragAndDropPage

class MainPage(Page):
    _url = '{base_url}'
    _loc_key_press_link = (By.XPATH, "//*[@href='/key_presses']")
    _loc_drag_and_drop_link = (By.XPATH, "//*[@href='/drag_and_drop']")

    def open_key_presses_page(self):
        self.selenium.find_element(*self._loc_key_press_link).click()
        key_press_page = KeyPressPage(self.base_url, self.selenium)
        return key_press_page

    def open_drag_and_drop_page(self):
        self.selenium.find_element(*self._loc_drag_and_drop_link).click()
        dnd_page = DragAndDropPage(self.base_url, self.selenium)
        return dnd_page
