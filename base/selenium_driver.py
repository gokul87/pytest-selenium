from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type is not supported")
        return False

    def getElement(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element is found")
        except:
            print("Element is not found")
        return element

    def getAllElements(self, locator, locatorType = "id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            print("Element is found")
            return elements
        except:
            print("Element is not found")
            return None

    def getTagName(self, tag):
        try:
            tags = self.driver.find_elements_by_tag_name(tag)
            return tags
        except:
            return None


    def elementClick(self, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Element is clicked")
        except:
            print("Element is not found to be clicked")

    def isElementPresent(self, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element is present")
                return True
            else:
                return False
        except:
            print("Element is not present")
            return False

    def waitForElement(self, locator, locatorType = "id",
                       timeout=10, pollfrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            wait  = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located((byType, locator)))
            print("Element is located in page")
        except:
            print("Element is not located in page")
        return element

    def sendKeys(self, data, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except:
            print("Data not entered")

    def getText(self, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            title = element.text
            print("The title is " + title)
            return title
        except:
            print("Text cannot be fetched")
            return None
