import json
import pytest

from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain browser')
    elif config['browser'] not in ['chrome', 'firefox']:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else 10

@pytest.fixture
def browser(config_browser, config_wait_time):

    # Initialize Browser
    if config_browser == 'chrome':
        driver = Chrome(ChromeDriverManager().install())
    elif config_browser == 'firefox':
        driver = Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()