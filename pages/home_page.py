from .base_page import BasePage
from ._locators import HomePageLocators

class HomePage(BasePage):
    expected_text = 'ATID Demo Store'
    def should_be_home_page(self):
        assert self.element_is_visible(HomePageLocators.WEBSITE_TITLE), "'Home' page title is not visible, that may be not ATID Store"
        text = self.get_visible_text(HomePageLocators.WEBSITE_TITLE)
        assert text == self.expected_text, "'Home' page title is not as expected" #f expected = {}, in reality = {}

    def click_cart_button(self):
        self.click_element(HomePageLocators.CART_BUTTON)
    
    def click_store_button(self):
        self.click_element(HomePageLocators.STORE_BUTTON) 

        
