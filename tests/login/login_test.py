import unittest
import pytest
from pages.login.login_page import LoginPage


@pytest.mark.usefixture("setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.lp = LoginPage(self.driver)

    def test_login(self):
        self.lp.verifyElementPresent()
        self.lp.clickSignIn()


if __name__ == "__main__":
    unittest.main()