from .base_page import BasePage
from ._locators import HomePageLocators

class HomePage(BasePage):
    expected_text = 'ATID Demo Store'
    def should_be_homepage(self):
        assert self.element_is_visible(HomePageLocators.MAIN_TITLE), "Main title is not visible"
        text = self.get_visible_text(HomePageLocators.MAIN_TITLE)
        assert text == self.expected_text, 'Not expected text of main title'
