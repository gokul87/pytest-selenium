import re
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

from base.selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def searchAProduct(self):
        self.isElementPresent('.z-navicat-header_searchInput', 'css')
        self.sendKeys('winter coat', '.z-navicat-header_searchInput', 'css')
        if self.isElementPresent('.z-navicat-header_searchForm span.z-icon-black', 'css'):
            self.sendKeys(u'\ue007', '.z-navicat-header_searchInput', 'css')
            sleep(3)
            #self.waitForElement(".srp-controls__control", "css")

    def verifyIfSearchIsSuccesfull(self):
        titleEle = self.getAllElements(".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF", "css")
        topTenProducts = len(titleEle) - 73

        for i in range(1, int(topTenProducts)):
            title = self.getElement(".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF:nth-child("+str(i)+") .z-nvg-cognac_articleName--arFp", "css").text
            if 'Winter' or 'coat' in title:
                print("The title of the product is "+ title)
                print("Test Successfully passed")
            else:
                print("Test failed")

    def sortByPrice(self):
        self.isElementPresent("z-grid-item:nth-child(3) .z-nvg-cognac_filterBox-2eHBH", "css")
        self.elementClick("z-grid-item:nth-child(3) .z-nvg-cognac_filterHead-3-7Lz", "css")
        sleep(2)

        if self.isElementPresent(".z-nvg-cognac_filter-UPD9y.z-nvg-cognac_filterActive-2tuDF", "css") is True:
            """ Move the slider to sort the prices"""
            # print("Can see the slider")
            slider = self.getElement('.input-range__slider-container:nth-child(2) div', 'css')
            move = ActionChains(self.driver)
            move.click_and_hold(slider).move_by_offset(40, 0).release().perform()
            sleep(2)

            #Submit the filtered price range
            self.elementClick("button.z-button--primary div.z-button__content", "css")
            self.waitForElement(".z-nvg-cognac_articles")

            #Sort the price by
            el = self.getElement(".z-nvg-cognac_dropdown-2Ii3R", "css")
            for option in el.find_elements_by_tag_name('option'):
                if option.text == "Lowest price":
                    option.click()
                    sleep(5)
                    break

    def fetchThePrice(self):
        global fList
        aList = []
        price = self.getAllElements(
            ".z-nvg-cognac_articles z-grid-item div .z-nvg-cognac_infoContainer-MvytX .z-nvg-cognac_prices-2-Zhx div",
            "css")
        fetchTopTenPrice = len(price) - 7

        for i in range(1, int(fetchTopTenPrice)):
            fetchPrice = self.getElement(".z-nvg-cognac_articles z-grid-item:nth-child(" + str(
                i) + ") div .z-nvg-cognac_infoContainer-MvytX .z-nvg-cognac_prices-2-Zhx div",
                                         "css").text

            pr = re.sub(r'[,|£|!|''|]', r'', fetchPrice)
            # aList = list(map(float, aList))
            aList.append(pr)

        fList = [float(i) for i in aList]
        print("The list is " + str(fList))

    def checkIfSorted(self):
        global fList
        # print("The length of list is " + str(len(aList)))
        """Verify if the list is sorted"""
        if fList == sorted(fList):
            print("List is sorted correctly")
        else:
            print("List is not sorted")

    def verifySorting(self):
        self.sortByPrice()
        self.fetchThePrice()
        self.checkIfSorted()

