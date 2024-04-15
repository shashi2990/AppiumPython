import logging
import time

from selenium.common import NoSuchElementException

from Utilities import configReader
from Utilities.LogUtil import Logger
from appium.webdriver.common.appiumby import AppiumBy

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def click(self, locator):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
    #     log.logger.info("Click on an Element", str(locator))

    def click(self, locator):
        locator_type = None
        element = None

        if str(locator).endswith("_XPATH"):
            locator_type = AppiumBy.XPATH
        elif str(locator).endswith("_ID"):
            locator_type = AppiumBy.ID
        elif str(locator).endswith("_ACCESSIBILITYID"):
            locator_type = AppiumBy.ACCESSIBILITY_ID

        if locator_type:
            element_locator = configReader.readConfig("locators", locator)

            try:
                element = self.driver.find_element(locator_type, element_locator)
                element.click()
                log.logger.info(f"Clicked on element using {locator_type}: {element_locator}")
            except NoSuchElementException:
                log.logger.warning(f"Element not found using {locator_type}: {element_locator}")
        else:
            log.logger.error("Invalid locator type provided")

        return element  # Return the element (if found) for further operations or assertions

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).senk_key(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).senk_key(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).senk_key(value)
        log.logger.info("Click on an Element", str(locator), "Enter the value as :", value)

    def getText(self, locator, text):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).text
        log.logger.info("Getting text from an Element", str(locator))
        return text

    def clickIndex(self, locator,index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Click on an Element", str(locator)+"with index : "+str(index))