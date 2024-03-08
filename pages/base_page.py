from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    #check element presence and visibility

    def find_element(self, locator: tuple, waiting=5):
        try:
            element = WebDriverWait(self.browser, waiting).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} does not exist on this page")
           

    def element_is_visible(self, locator: tuple, waiting = 5) -> bool:
        try:
            WebDriverWait(self.browser, waiting).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
#locator = 1, no args, in WebDriverWait

    def element_is_not_present(self, locator: tuple, waiting = 5) -> bool:
        try:
            WebDriverWait(self.browser, waiting).until(
                EC.presence_of_element_located(locator)
            )
            return False                
        except TimeoutException:
            return True

# TimeoutException - для явного ожидания отлавливаем

    def element_is_not_visible(self, locator: tuple, waiting = 5) -> bool:
        try:
            WebDriverWait(self.browser, waiting).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False 
    
    def element_disappeared(self, locator: tuple, waiting = 5):
        return not self.element_is_visible(locator, waiting)
    
    #clicks

    def click_element(self, locator: tuple, waiting = 5):
        try:
            elem = WebDriverWait(self.browser, waiting).until(
                EC.element_to_be_clickable(locator)
            )
            elem.click()
        except TimeoutException:
            raise AssertionError(f'Element with locator {locator} is not clickable')
        
    def click_after_scroll(self, locator: tuple, waiting = 5):
        try:
           elem = WebDriverWait(self.browser, waiting).until(
               EC.element_to_be_clickable(locator)
           )
           action = ActionChains(self.browser)
           action.scroll_to_element(elem).perform()
           action.click(elem)
        except TimeoutException:
            raise AssertionError(f'Element with locator {locator} is not clickable')

    def element_is_not_clickable(self, locator: tuple, waiting = 5):
        while(True):
            try:
                WebDriverWait(self.browser, waiting).until(
                EC.element_to_be_clickable(locator)
                )
            except:
                break

    #read elements
        
    def get_visible_text(self, locator: tuple) -> str:
        try:
            return self.browser.find_element(*locator).text
        except NoSuchElementException:
            raise AssertionError(f'No text from element {locator} received')

    #lists
        
    def get_list_of_elements(self, locator: tuple):
        elements = self.browser.find_element(*locator)
        if len(elements): 
            return elements
        else:
            raise AssertionError(f'Failed to find list of elements: {locator}')

        
