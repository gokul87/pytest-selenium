import unittest
from tests.home.home_test import HomeTest
from tests.login.login_test import LoginTest
from tests.product.product_test import ProductTest

#Get all tests from homepage, login and product test
ho_test = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
lo_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
po_test = unittest.TestLoader().loadTestsFromTestCase(ProductTest)

#create a  test suite
test_suite = unittest.TestSuite([ho_test, lo_test, po_test])

#Run the suite
unittest.TextTestRunner().run(test_suite)