from traceback import print_stack
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'tag':
            return By.TAG_NAME
        elif locatorType == 'name':
            return By.NAME
        else:
            self.log.info("Locator type " + locatorType + " not supported")
            return None

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found with locator: ' + locator + " and locator type: "+ locatorType)
        except:
            self.log.error('Element not found with locator: ' + locator + " and locator type: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        :param locator:
        :param locatorType:
        :return:
        """
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element list not found with locator: " + locator + " and locatorType: "+ locatorType)
        return elements

    def clickElement(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorTyepe
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            element.send_keys(Keys.HOME)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide an element or a combination of locator and locatorType

        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator + " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locatorType: " + locatorType)
                return False
        except:
            self.log.error('Element not found')
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide an element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locatorType: " + locatorType)
            else:
                self.log.info("Element is not displayed with locator: " + locator + " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element not found")
            return False

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get text of an element
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting the text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get the text on element " + info)
            print_stack()
            text = None
        return text

    def checkElementPresent(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info('Element found')
                return True
            else:
                return False
        except:
            self.log.error('Element not found')
            return False


    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType.lower())
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                   ElementNotVisibleException,
                                                                                   ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info('Element appeared on the web page')

        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def screenShot(self, resultMessage):
        """
        Takes screenshot of currently open web page
        :param resultMessage:
        :return:
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "screenshots\\"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, '..', relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screesnshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def scrollWebPage(self, direction="up"):
        """
        Scroll webpage
        :param direction: up or down
        :return:
        """
        if direction == "up":
            # Scroll up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # scroll down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def clickUsingJavascript(self, locator="", locatorType="id", element=None):
        try:
            element = None
            if locator:
                element = self.getElement(locator, locatorType)
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info("Clicked on element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Unable to click on element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def switchToFrame(self, iframeElement):
        try:
            self.driver.switch_to.frame(iframeElement)
            self.log.info("Switched to iframe: " + str(iframeElement))
        except:
            self.log.error("Unable to switch to iframe: " + str(iframeElement))
            print_stack()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of the element
        :param attribute: attribute whose  value to find
        :param element: Element whose attribute we need to find
        :param locator: locator of the element
        :param locatorType: locator type to find the element
        :return: value of the attribute
        """
        if locator:
            element = self.getElement(locator, locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self,locator, locatorType="id", info=""):
        """
        Check if element is enabled
        :param locator: locator of the element to check
        :param locatorType: Type of the locator(id(default), xpath, css, className, linkText)
        :param info: Information about the element, label/name of the element
        :return: boolean
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(attribute="disabled", element=element)
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value from application web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: " + info + " state could not be found")
        return enabled

    def switchFrameByIndex(self, locator="", locatorType="xpath"):
        """
        Get iframe using element locator inside iframe
        :param locator: locator of the element
        :param locatorType: locator type to find the element
        :return: index of frame
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", "xpath")
            self.log.info("Length of the iframe list :: " + str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is :: " + str(i))
                    break
                self.driver.switch_to.default_content()
            return result
        except:
            self.log.error("iframe index not found")
            return result