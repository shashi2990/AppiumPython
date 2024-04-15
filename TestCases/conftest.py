import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.android import UiAutomator2Options
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["device1"], scope="function")
def appium_driver(request):
    # global appium_service
    global driver
    # appium_service = AppiumService()
    # appium_service.start()
    # print(appium_service.is_listening)
    if request.param == "device1":
        desired_caps = dict(
            deviceName="Android",
            platformName="Android",
            udid="RZ8N92L0JQV",
            # browserName="Chrome"
            appActivity="com.goibibo.common.HomeActivity",
            appPackage="com.goibibo",
            noReset=True
        )
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)
    if request.param == "device2":
        desired_caps = dict(
            deviceName="Android",
            platformName="Android",
            udid="RZ8N92L0JQV",
            # browserName="Chrome"
            appActivity="com.goibibo.common.HomeActivity",
            appPackage="com.goibibo",
            noReset=True
        )
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    # appium_service.stop()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
