from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidCardNumber(self):
        self.courses.selectCourseToEnroll("Javascript")
        self.courses.enrollCourse("1234567812345678", "05/23", "123")
        result = self.courses.verifyInvalidCardNumber()
        self.ts.mark(result, "Card Number is invalid")
