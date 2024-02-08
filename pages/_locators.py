from selenium.webdriver.common.by import By

class HomePageLocators:
    MAIN_TITLE = (By.CSS_SELECTOR, ".elementor-widget-container h1")
    STORE_BUTTON = (By.CSS_SELECTOR, "#menu-item-45 a")

class StorePageLocators:
    CATEGORIES_LIST = (By.CSS_SELECTOR, ".product-categories li a")

