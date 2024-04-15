import time

from Pages.BasePage import BasePage
from Pages.HourlyStays import HourlyStays


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoHotels(self):
        pass

    def gotoVillas(self):
        pass

    def gotoHourlyStays(self):
        time.sleep(8)
        self.click("homeEmpty_XPATH")
        time.sleep(2)
        self.click("hourlyStays_XPATH")
        return HourlyStays(self.driver)

    def gotoFlights(self):
        pass

