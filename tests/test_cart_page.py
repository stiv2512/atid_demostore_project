import pytest
from pages.cart_page import CartPage
from pages.Item_page import ItemPage
from pages.home_page import HomePage
from selenium.webdriver import Chrome

@pytest.mark.cart
class TestCartPage:

    cart_url = 'https://atid.store/cart-2/'
    store_url = 'https://atid.store/store/'

    def test_user_can_access_to_cart_page(self, browser):
        cart_page = CartPage(browser, self.cart_url)
        cart_page.open()
        cart_page.should_be_cart_page()

    def test_item_added_by_user_is_present(self, browser: Chrome):
        """проверить, что конкретный товар добавлен"""
        page = ItemPage(browser, "https://atid.store/product/dnk-tshirt/")
        page.open()
        page.should_be_chosen_item("ATID Green Tshirt")
        page.click_add_to_cart()
        page = HomePage(browser, browser.current_url)
        page.click_cart_button()
        page = CartPage(browser, browser.current_url)
        page.should_be_cart_page()
        page.should_be_added_item("ATID Green Tshirt")

    # done - поменять число товаров -> update cart


    # pip install pytest-rerunfailures
    def test_update_cart(self, browser: Chrome):
        page = ItemPage(browser, "https://atid.store/product/dnk-tshirt/")
        page.open()
        page.should_be_chosen_item("ATID Green Tshirt")
        page.click_add_to_cart()
        page = CartPage(browser, self.cart_url)
        page.open()
        page.should_be_cart_page()
        page.should_be_added_item("ATID Green Tshirt")
        page.change_item_number(2)
        page.click_update_button()
        page.check_subtotal_price("3,990.00")

    # done - удалить товар -> undo
    @pytest.mark.last    
    def test_delete_undo(self, browser: Chrome):
        page = ItemPage(browser, "https://atid.store/product/dnk-tshirt/")
        page.open()
        page.should_be_chosen_item("ATID Green Tshirt")
        page.click_add_to_cart()
        page = CartPage(browser, self.cart_url)
        page.open()
        page.should_be_cart_page()
        page.should_be_added_item('ATID Green Tshirt')
        page.delete_item_from_cart()
                                             

        

               