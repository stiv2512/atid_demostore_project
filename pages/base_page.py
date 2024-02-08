from selenium.webdriver import Chrome

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # PRESENCE OF ELEMENTS
    def element_is_present(self):
        pass

    def element_is_visible(self):
        pass

    def element_is_not_present(self):
        pass

    def element_is_not_visible(self):
        pass

    # CLICKS

    def click_element(self):
        pass

    def click_after_scroll(self):
        pass

    #Reading function

    def get_visible_text(self):
        pass