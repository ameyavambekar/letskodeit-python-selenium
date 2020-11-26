from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.navigation = NavigationPage(self.driver)

    def setUp(self):
        self.navigation.navigateToAllCourses()


    @pytest.mark.run(order=1)
    @data(*getCSVData("D:\python-workspace\letskodeit\\testdata.csv"))
    @unpack
    def test_invalidCardNumber(self, courseName, ccNum, ccExp, ccCvc):
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(ccNum, ccExp, ccCvc)
        result = self.courses.verifyInvalidCardNumber()
        self.ts.markFinal("test_invalidCardNumber", result, "Card Number is invalid")