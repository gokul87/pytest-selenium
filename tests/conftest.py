import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="class")
def setup(request):
    baseurl = "https://www.zalando.co.uk/"

    desired_cap = {
        'browserName': "chrome",
        'name': "Tharunikha test",
    }
    #driver = webdriver.Firefox(executable_path='/home/tharu/Downloads/geckodriver')
    #driver = webdriver.Chrome(executable_path='/home/tharu/Downloads/chromedriver')
    #driver = webdriver.Remote("http://localhost:4444/wd/hub",DesiredCapabilities.CHROME,"Test name")
    driver = webdriver.Remote("http://localhost:4444/wd/hub",
                            desired_capabilities = desired_cap)
    driver.implicitly_wait(3)
    driver.get(baseurl)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
