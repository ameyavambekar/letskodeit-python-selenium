from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("Javascript", "1234567812345678", "05/23", "123"), ("Complete Test Automation Bundle", "1234567812345678", "05/23", "123"))
    @unpack
    def test_invalidCardNumber(self, courseName, ccNum, ccExp, ccCvc):
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(ccNum, ccExp, ccCvc)
        result = self.courses.verifyInvalidCardNumber()
        self.ts.markFinal("test_invalidCardNumber", result, "Card Number is invalid")
        self.driver.find_element_by_xpath("//a[text()='ALL COURSES']").click()


    # @pytest.mark.run(order=2)
    # def test_invalidExpDate(self):
    #     self.courses.enrollCourse("4018061875027108", "05/20", "123")
    #     result = self.courses.verifyInvalidExpiryDate()
    #     self.ts.markFinal("test_invalidExpDate", result, "Expiration date is passed")