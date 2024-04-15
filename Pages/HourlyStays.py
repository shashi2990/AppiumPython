import time

from Pages.BasePage import BasePage


class HourlyStays(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def searchHourlyHotel(self, city):
        time.sleep(5)
        self.click("destination_XPATH")
        time.sleep(2)
        self.click("searchText_XPATH", city)
        time.sleep(2)
        self.click("selectLocation_XPATH", 9)
        time.sleep(2)
        self.click("searchButton_XPATH")