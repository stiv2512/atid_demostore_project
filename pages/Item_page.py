from .base_page import BasePage
from ._locators import ItemPageLocators

class ItemPage(BasePage):
    def should_be_chosen_item(self, expected_text):
        assert self.element_is_visible(ItemPageLocators.ITEM_TITLE), 'Not chosen item is displayed'
        text = self.get_visible_text(ItemPageLocators.ITEM_TITLE)
        assert text == expected_text, f"Expected {expected_text}, received {text}"

    def click_add_to_cart(self):
        self.click_element(ItemPageLocators.ADD_TO_CART)