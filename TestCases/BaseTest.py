import pytest


@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest:
    pass
