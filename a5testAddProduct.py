import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# inherit TestCase Class and create a new test class
class A5TestCaseAddProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(r"C:\MicrosoftWebDriver.exe")

    # Test case method. It should always start with test_
    def test_a5testAddProduct(self):

        user = "instructor"
        pwd = "gounomavs1a"
        # get driver
        driver = self.driver
        # get app
        driver.get("https://rentapp-assignment5.herokuapp.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)

        # click login
        driver.find_element_by_xpath('//*[@id="navbarNav"]/form/a[1]').click()
        time.sleep(1)
        # click username
        driver.find_element_by_xpath('//*[@id="id_username"]').click()
        # enter username
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        # click password
        elem = driver.find_element_by_id("id_password")
        # enter password
        elem.send_keys(pwd)
        # click logon
        driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        time.sleep(2)

        name = "TestCaseItem"
        cost = "45"
        desc = "This is a wonderful test description!"

        driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[3]/h4/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="addBtn"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="id_itemName"]').click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_itemName")
        elem.send_keys(name)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="id_category"]/option[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="id_costPerItem"]').click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_costPerItem")
        elem.send_keys(cost)
        elem = driver.find_element_by_id("id_itemDescription")
        elem.send_keys(desc)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="backend_upload"]/input[2]').click()
        time.sleep(3)
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()