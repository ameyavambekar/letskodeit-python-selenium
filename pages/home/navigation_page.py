import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo_link = "//a[contains(@class,'logo')]"
    _home_link = "//a[text()='HOME']"
    _all_courses_link = "//a[text()='ALL COURSES']"
    _support_link = "//a[text()='SUPPORT']"
    _my_courses_link = "//a[text()='MY COURSES']"
    _my_profile_link = "//button[@id='dropdownMenu1']"

    def navigateToAllCourses(self):
        self.clickElement(self._all_courses_link, "xpath")
        time.sleep(3)

    def navigateToHome(self):
        self.clickElement(self._home_link, "xpath")
        time.sleep(3)

    def navigateToSupport(self):
        self.clickElement(self._support_link, "xpath")
        time.sleep(3)

    def navigateToMyCourses(self):
        self.clickElement(self._my_courses_link, "xpath")
        time.sleep(3)

    def navigateToProfile(self):
        self.clickElement(self._my_profile_link, "xpath")
        time.sleep(3)

    def clickSignInLink(self):
        self.clickElement(self._login_link, "xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.clickElement(self._login_button, "xpath")

    def login(self, userName="", password=""):
        self.clickSignInLink()
        self.clearFields()
        self.enterEmail(userName)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        return self.isElementPresent(self._dropdown_menu, 'xpath')

    def verifyLoginFailed(self):
        return self.isElementPresent(self._error_message, 'xpath')

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()

    def verifyTitle(self):
        return self.verifyPageTitle("Google")