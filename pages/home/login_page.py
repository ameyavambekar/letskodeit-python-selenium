import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation = NavigationPage(driver)

    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"
    _dropdown_menu = "//button[@id='dropdownMenu1']//img"
    _error_message = "//input[@id='email']//following-sibling::span"

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
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.navigation.navigateToProfile()
        self.clickElement("//a[text()='Logout']", "xpath")


