from pypom import Page
from .key_press_page import KeyPressPage


class Base(Page):
    def __init__(self, selenium, base_url, variables):
        self.v = variables
        super(Base, self).__init__(selenium, base_url)
