from selene import Browser, Config
from selene.support.shared import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test import attach

@pytest.fixture(scope='function')
def jenkins_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    browser.quit()










@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options  # чтоб тест выполнялся когда сайт продолжается грузиться , но html загрузился
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # driver_options = webdriver.ChromeOptions()   #настройка чтоб не открывать браузер , надо для этого 8 , 10 строчку кода
    # driver_options.add_argument('--headless')
    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    browser.quit()




