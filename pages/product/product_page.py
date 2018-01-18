from base.selenium_driver import SeleniumDriver
from selenium import webdriver


class ProductPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def getProductTitle(self):
        fetchTitle = self.getElement(".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF:nth-child(1) .z-nvg-cognac_articleName--arFp",
                        "css").text

        return fetchTitle

    def getProductPrice(self):
        fetchPrice = self.getElement(
            ".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF:nth-child(1) .z-nvg-cognac_originalPrice-2Oy4G",
            "css").text

        return fetchPrice


    def selectProduct(self):
        self.elementClick(".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF:nth-child(1) div a.z-nvg-cognac_imageLink-OPGGa div",
                          "css")
        self.waitForElement("#z-pdp-topSection-addToCartButton","css")


    def verifyProductTitle(self):
        title = self.getElement("div.h-product-title h1", "css").text

        return title

    def verifyProductPrice(self):
        price = self.getElement("div.h-product-price h4", "css").text

        return price