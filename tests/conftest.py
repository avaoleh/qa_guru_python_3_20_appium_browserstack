import allure_commons
import allure
import pytest
from selene.support.shared import browser
from selene import support
from appium import webdriver
import config
from mobile_tests_appium import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)
    browser.config.driver = webdriver.Remote(config.settings.remote_url, options=config.settings.driver_options)
    browser.config.timeout = config.settings.timeout

    yield

    session_id = browser.driver.session_id

    allure.step('close app session')(browser.quit)()

    utils.allure.attach.video_from_browserstack(session_id)
