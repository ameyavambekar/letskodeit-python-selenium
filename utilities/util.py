"""
Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()

"""
import time
from traceback import print_stack
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        :param sec:
        :param info:
        :return:
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        """
        Get random string of characters
        :param length: number of characters the string should have
        :param type: Type of characters the string should have. Default is lettes
        Provide upper/lower/digits for different types
        :return:
        """
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphaNumeric(charCount, "lower")

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids
        :param listSize: Number of email ids. Default is 5 email in a list
        :param itemLength: It should be a list containing number of items equal to the listSize
        This determines the length of each item in the list
        :return:
        """
        nameList = []
        for i in range(listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text from Web UI ---> :: " + actualText)
        self.log.info("Expected Text ---> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT CONTAIN !!!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify Text Match
        :param self:
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text from UI ---> :: " + actualText)
        self.log.info("Expected Text  ---> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page title
        :param titleToVerify:
        :return:
        """
        try:
            actualTitle = self.getTitle()
            return self.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        :param expectedList: Expected List
        :param actualList: Actual List
        :return:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        :param expectedList: Expected List
        :param actualList: Actual List
        :return:
        """
        length = len(expectedList)
        for i in range(length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True