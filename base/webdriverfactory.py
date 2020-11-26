"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
import os


class WebDriverFactory():


    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        :param browser:
        :returns: None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS        
        chromedriver = "path to chrome driver"
        os.environ["webdriver.chorme.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        PREFERRED: Set the path on the machine where browser will be executed       
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on browser configuration

        :return: WebDriver Instance
        """
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == 'iexplorer':
            driver = webdriver.Ie()
        elif self.browser == 'chrome':
            chromedriver = "D:\drivers\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1920, 1080)
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        return driver

