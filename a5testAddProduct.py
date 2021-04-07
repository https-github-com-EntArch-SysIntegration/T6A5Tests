import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# inherit TestCase Class and create a new test class
class A5TestCaseLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(executable_path="c:\MicrosoftWebDriver.exe")

    # Test case method. It should always start with test_
    def a5testAddProduct(self):

        user = "instrustor"
        pwd = "gounomavs1a"
        # get driver
        driver = self.driver
        driver.maximize_window()
        # get app
        driver.get("https://rentapp-assignment5.herokuapp.com/")
        time.sleep(1)

        # click login
        elem = driver.find_element_by_xpath('//*[@id="navbarNav"]/form/a[1]').click()
        # click username
        elem = driver.find_element_by_id("id_username").click()
        # enter username
        elem.send_keys(user)
        # click password
        elem = driver.find_element_by_id("id_password").click()
        # enter password
        elem.send_keys(pwd)
        # click logon
        elem = driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        time.sleep(2)

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
