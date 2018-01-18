from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyElementPresent(self):
        self.isElementPresent("div.z-navicat-header_userAccOverlay a div.z-button__content:nth-child(1)",
                              "css")

    def clickSignIn(self):
        self.elementClick("div.z-navicat-header_userAccOverlay a div.z-button__content:nth-child(1)",
                          "css")
        self.waitForElement("button.z-button:nth-child(1) div.z-button__content", "css")