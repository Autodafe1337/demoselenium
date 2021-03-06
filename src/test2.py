from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        titles = driver.find_elements_by_id('LC20lb')
        for title in titles:
            assert 'python' in title.text.lower()

    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        input_field.send_keys('python')
        time.sleep(1)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        titles = driver.find_elements_by_id('LC20lb')
        for title in titles:
            assert 'python' in title.text.lower()


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()