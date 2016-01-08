from selenium.webdriver.common.by import By
from pypom import Page
from selenium.webdriver.common.action_chains import ActionChains

class DragAndDropPage(Page):
    _url = '{base_url}/drag_and_drop'
    _loc_column_a = (By.XPATH, ".//*[@id='column-a']")
    _loc_column_b = (By.XPATH, ".//*[@id='column-b']")
    _loc_column_a_header = (By.XPATH, ".//*[@id='column-a']/header")
    _loc_column_b_header = (By.XPATH, ".//*[@id='column-b']/header")

    def drag_source_to_target(self, source, target):
        action = ActionChains(self.selenium)
        #action.drag_and_drop(source, target)
        custom_source = self.selenium.find_element(*self._loc_column_a)
        print(custom_source.get_attribute("draggable"))
        print(custom_source.get_attribute("id"))
        custom_target = self.selenium.find_element(*self._loc_column_b)
        print(custom_target.get_attribute("id"))
        action.drag_and_drop(custom_source,custom_target)
        action.perform()

    @property
    def column_a(self):
        return self.selenium.find_element(*self._loc_column_a)

    @property
    def column_b(self):
        return self.selenium.find_element(*self._loc_column_b)

    @property
    def column_a_header(self):
        return self.selenium.find_element(*self._loc_column_a_header).text

    @property
    def column_b_header(self):
        return self.selenium.find_element(*self._loc_column_b_header).text
