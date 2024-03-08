from pages.home_page import HomePage
import pytest

@pytest.mark.home
class TestHomePage:
    
    def test_user_can_access_to_home_page(self, browser):
        self.url = 'https://atid.store/'
        self.home_page = HomePage(browser, self.url)
        self.home_page.open()
        self.home_page.should_be_home_page()
