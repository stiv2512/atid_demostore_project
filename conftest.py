import pytest
from selenium import webdriver

def pytest_addoption(parser: pytest.Parser):
    """
    parser.addoption(
    action: How the variable is saved
        'store': str 
        'store_true': boolean 
        'store_false': boolean 
    default: The default definition of variable saved
    help: Description of the variable
    )
    """
    parser.addoption('--headless', action = 'store_true', help = 'Type "--headless" to start browser in this mode')
    parser.addoption('--lang', action = 'store', default = 'en-US', help = 'Set up your browser language, Russian is chosen in default')
    parser.addoption('--size', action = 'store', default="", help = 'Choose window size parametres')
    parser.addoption('--maximized', action = 'store_true', help = 'Full screen mode is on in default')
    parser.addoption('--incognito', action = 'store_true', help = 'Type "--incognito" to switch to Google Chrome Incognito mode')
    parser.addoption('--disable-gpu', action = 'store_true', help = 'Start browser in "light" mode')

@pytest.fixture(scope='function')   
def browser(request: pytest.FixtureRequest):
    options = webdriver.ChromeOptions()
    headless = request.config.getoption('headless')
    size_max = request.config.getoption('maximized')
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    elif size_max:
        options.add_argument("--start-maximized")
    else:
        size = request.config.getoption("size")
        options.add_argument(f"--window-size={size}")
    lang = request.config.getoption('lang')
    options.add_argument(f'--lang={lang}')
    incognito = request.config.getoption("incognito")
    if incognito:
        options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()




