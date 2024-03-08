from selenium.webdriver.common.by import By

class HomePageLocators:
    WEBSITE_TITLE = (By.CSS_SELECTOR, 'style ~ .elementor-heading-title')
    CART_BUTTON = (By.CSS_SELECTOR, '.ast-cart-menu-wrap') #'div > .cart-container') #.ast-cart-menu-wrap
    STORE_BUTTON = (By.CSS_SELECTOR, '#menu-item-45 > a')

class StorePageLocators:
    FILTER_BY_PRICE = (By.CSS_SELECTOR, '#woocommerce_price_filter-2 > .widget-title')
    ITEM_LINK = (By.CSS_SELECTOR, '#woocommerce_top_rated_products-1 > ul > li:nth-child(1) > a')

class ItemPageLocators:
    ITEM_TITLE = (By.CSS_SELECTOR, 'h1.product_title')
    ADD_TO_CART = (By.CSS_SELECTOR, '.single_add_to_cart_button')

class CartPageLocators:
    CART_TITLE = (By.CSS_SELECTOR, '.elementor-heading-title.elementor-size-default')
    ITEM_IN_CART = (By.CSS_SELECTOR, 'td.product-name > a')
    ITEM_NUMBER = (By.CSS_SELECTOR, "[type='number']")
    UPDATE_CART = (By.CSS_SELECTOR, 'div ~ button')
    SUBTOTAL_PRICE = (By.CSS_SELECTOR, 'td.product-subtotal > span > bdi')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'td .remove')
    UNDO = (By.CSS_SELECTOR, 'div.woocommerce-message > a')

