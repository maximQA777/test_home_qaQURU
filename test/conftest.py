
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    #driver_options = webdriver.ChromeOptions()   #настройка чтоб не открывать браузер
    #driver_options.add_argument('--headless')
    #browser.config.driver_options = driver_options
    yield
    browser.quit()