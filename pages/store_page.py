from .base_page import BasePage
from ._locators import StorePageLocators

class StorePage(BasePage):
    def should_be_store_page(self, expected_text):
        assert self.element_is_visible(StorePageLocators.FILTER_BY_PRICE), "'Filter by Price' heading does not exist, this may not be a 'Home' page"
        text = self.get_visible_text(StorePageLocators.FILTER_BY_PRICE)
        assert text == expected_text, f'Expected {expected_text}, got {text}'
    
    def click_item_link(self):
        self.click_element(StorePageLocators.ITEM_LINK)
