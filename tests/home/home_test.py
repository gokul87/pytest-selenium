import unittest
import pytest
from pages.home.home_page import HomePage

@pytest.mark.usefixtures("setup")
class HomeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, setup):
        self.hp = HomePage(self.driver)

    def test_search(self):
        self.hp.searchAProduct()
        self.hp.verifyIfSearchIsSuccesfull()

    #def test_sorting(self):
        #self.hp.searchAProduct()
        # self.hp.verifySorting()


if __name__ == "__main__":
    unittest.main()