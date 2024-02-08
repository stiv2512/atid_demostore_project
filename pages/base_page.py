from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # PRESENCE OF ELEMENTS
    def element_is_present(self):
        pass

    def element_is_visible(self, locator: tuple, waiting=5) -> bool:
        try:
            WebDriverWait(self.browser, waiting).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    def element_is_not_present(self):
        pass

    def element_is_not_visible(self, locator: tuple, waiting=5) -> bool:
        try:
            WebDriverWait(self.browser, waiting).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def element_disappeared(self, locator: tuple, waiting=5):
        return not self.element_is_visible(locator, waiting)

    # CLICKS

    def click_element(self):
        pass

    def click_after_scroll(self):
        pass

    #Reading function

    def get_visible_text(self):
        pass