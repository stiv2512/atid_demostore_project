from pages.home_page import HomePage
import pytest



@pytest.mark.home
class TestHomePage:

    url = 'https://atid.store/'
    
    def setup_method(self, browser):
        self.home_page = HomePage(browser, self.url)
        self.home_page.open()
    
    @pytest.mark.smoke
    def test_user_can_access_to_home_page(self):
        self.home_page.should_be_home_page()

    def test_user_can_click_store_button(self):
        pass
    
