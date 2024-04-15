import pytest

from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_HourlyStays(BaseTest):

    @pytest.mark.parametrize("city", dataProvider.get_data("LoginTest"))
    def test_hourlyStays(self, city, appium_driver):
        self.driver = appium_driver
        home = HomeScreen(self.driver)
        home.gotoHourlyStays().searchHourlyHotel(city)


