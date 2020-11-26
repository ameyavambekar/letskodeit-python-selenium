from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time
from selenium.webdriver.common.keys import Keys


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_box = "//input[@id='search']"
    _course_link = "//div[@id='course-list']//a"
    _all_courses = "//div[@id='course-list']//a"
    _enroll_button = "//button[contains(text(),'Enroll')]"
    _cc_num = "//input[@name='cardnumber' and not(@aria-hidden='true')]"
    _cc_exp = "//input[@name='exp-date' and not(@aria-hidden='true')]"
    _cc_cvc = "//input[@name='cvc' and not(@aria-hidden='true')]"
    _buy_button = "//button[contains(@class,'checkout-button')][1]"
    _invalid_card_number = "//span[text()='Your card number is invalid.']"
    _invalid_expiry_date = "//span[contains(text(),'expiration date')]"
    _expiration_date_frame = "//iframe[@title='Secure expiration date input frame']"
    _card_number_frame = "//iframe[@title='Secure card number input frame']"
    _cvc_frame = "//iframe[@title='Secure CVC input frame']"

    def enterCourseName(self, name):
        self.clickElement(self._search_box, "xpath")
        self.sendKeys(name, self._search_box, "xpath")
        self.sendKeys(Keys.ENTER, self._search_box, "xpath")
        time.sleep(3)

    def selectCourseToEnroll(self, fullCourseName):
        self.enterCourseName(fullCourseName)
        self.clickUsingJavascript(self._course_link, "xpath")
        # self.clickElement(self._course_link, "xpath")
        time.sleep(5)
        self.clickEnrollInCourseButton()

    def clickEnrollInCourseButton(self):
        self.clickElement(self._enroll_button, "xpath")

    def enterCardNum(self, num):
        self.switchToFrame(self.getElement(self._card_number_frame, "xpath"))
        cardNumber = self.getElement(self._cc_num, "xpath")
        cardNumber.clear()
        self.sendKeys(num, self._cc_num, "xpath")

    def enterCardExp(self, exp):
        self.switchToFrame(self.getElement(self._expiration_date_frame, "xpath"))
        expiryDate = self.getElement(self._cc_exp, "xpath")
        expiryDate.clear()
        self.sendKeys(exp, self._cc_exp, "xpath")

    def enterCardCvc(self, cvcNum):
        self.switchToFrame(self.getElement(self._cvc_frame, "xpath"))
        cvc = self.getElement(self._cc_cvc, "xpath")
        cvc.clear()
        self.sendKeys(cvcNum, self._cc_cvc, "xpath")

    def clickBuyButton(self):
        self.clickElement(self._buy_button, "xpath")

    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.driver.switch_to.default_content()
        self.enterCardExp(exp)
        self.driver.switch_to.default_content()
        self.enterCardCvc(cvc)
        self.driver.switch_to.default_content()

    def enrollCourse(self, num="", exp="", cvc=""):
        self.scrollWebPage("down")
        self.enterCreditCardInformation(num, exp, cvc)
        self.clickBuyButton()

    def verifyInvalidCardNumber(self):
        return self.isElementDisplayed(self._invalid_card_number, "xpath")

    def verifyInvalidExpiryDate(self):
        return self.isElementDisplayed(self._invalid_expiry_date, "xpath")

    def clearFields(self):

        self.driver.switch_to.default_content()
        self.switchToFrame(self.getElement(self._expiration_date_frame, "xpath"))

        self.driver.switch_to.default_content()
        self.switchToFrame(self.getElement(self._cvc_frame, "xpath"))
