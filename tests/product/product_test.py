import unittest
import pytest
from pages.home.home_page import HomePage
from pages.product.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class ProductTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, setup):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)

    def test_product_details(self):

        self.hp.searchAProduct()
        self.hp.verifyIfSearchIsSuccesfull()
        fTitle = self.pp.getProductTitle()
        fPrice = self.pp.getProductPrice()
        self.pp.selectProduct()
        tit = self.pp.verifyProductTitle()
        pri = self.pp.verifyProductPrice()

        self.assertIn(tit, fTitle)
        #self.assertIn(pri, fPrice)

if __name__ == "__main__":
    unittest.main()