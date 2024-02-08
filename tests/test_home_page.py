from pages.home_page import HomePage
import pytest

url = 'https://atid.store/'

@pytest.mark.smoke
@pytest.mark.home
def test_user_can_access_to_home_page(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.should_be_home_page()
    