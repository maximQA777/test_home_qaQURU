
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'   #чтоб тест выполнялся когда сайт продолжается грузиться , но html загрузился
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    #driver_options.add_argument('--headless')  #настройка чтоб не открывать браузер
    #browser.config.driver_options = driver_options
    yield
    browser.quit()