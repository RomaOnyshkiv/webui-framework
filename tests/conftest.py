import glob
import json
import os

import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions, Safari

CONFIG_FILE = 'tests/config.json'
SUPPORTED_BROWSERS = ['chrome', 'firefox', 'safari']
DEFAULT_WAIT = 20


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_FILE) as conf_file:
        data = json.load(conf_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT


@pytest.fixture(scope='session')
def chrome_options(config):
    chrome_options = ChromeOptions()
    if 'headless' in config:
        if config['headless']:
            chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    return chrome_options


@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time, chrome_options):
    __clean_up()
    if config_browser == 'chrome':
        driver = Chrome(options=chrome_options, service_args=['--verbose', '--log-path=logs/chromedriver.log'])
    elif config_browser == 'firefox':
        driver = Firefox(service_log_path='logs/firefox.log')
    elif config_browser == 'safari':
        driver = Safari(quiet=True)
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


def __clean_up():
    logs = glob.glob("logs/*")
    for l in logs:
        os.remove(l)
