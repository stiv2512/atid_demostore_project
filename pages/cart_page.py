from .base_page import BasePage
from ._locators import CartPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    def should_be_cart_page(self):
        assert self.element_is_visible(CartPageLocators.CART_TITLE), "'Cart' page title is not visible, that may not be 'Cart' page"
        text = self.get_visible_text(CartPageLocators.CART_TITLE)
        assert text == 'Cart', f"'Cart' page title is not as expected, received: {text}"

    def should_be_added_item(self, expected_text):
        assert self.element_is_visible(CartPageLocators.ITEM_IN_CART)
        text = self.get_visible_text(CartPageLocators.ITEM_IN_CART)
        assert text == expected_text, f'Expected {expected_text}, received {text}'
    
    def change_item_number(self, number: int):
        item_number_field = self.find_element(CartPageLocators.ITEM_NUMBER)
        item_number_field.send_keys(str(number))
        
    def click_update_button(self):
        self.click_element(CartPageLocators.UPDATE_CART)

    def check_subtotal_price(self, price: str):
        self.element_is_not_clickable(CartPageLocators.UPDATE_CART)
        text = self.get_visible_text(CartPageLocators.SUBTOTAL_PRICE)
        assert price in text, f'Expected {price}, received {text}'

    def delete_item_from_cart(self, waiting = 5):
        try:
            self.click_element(CartPageLocators.DELETE_BUTTON)
            WebDriverWait(self.browser, waiting).until(
                EC.element_to_be_clickable(CartPageLocators.UNDO)
            )
            return True
        except TimeoutException:
            raise AssertionError(f'Element does not exist on this page')