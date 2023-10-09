import pytest
from selene import browser
from webdriver_manager.core import driver
from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
