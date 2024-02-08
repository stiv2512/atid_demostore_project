from .base_page import BasePage
from ._locators import StorePageLocators

class StorePage(BasePage):
    def should_be_store_page(self):
        categories_list = self.get_list_of_elements(StorePageLocators)
        assert len(categories_list) == 3, f'There is not enough categories on the page, found {len(categories_list)}'