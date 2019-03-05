from selenium import webdriver
import unittest


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'http://www.old.practicalsqa.net/wp-login.php?redirect_to=http%3A%2F%2Fwww.old.practicalsqa.net%2F&reauth=1')
        self.driver.implicitly_wait(2)

    def test_01(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="rememberme"]').click()
        driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
        driver.implicitly_wait(2)
        print(driver.title.lower())
        assert 'practical sqa' == driver.title.lower()

    def test_02(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="rememberme"]').click()
        driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
        print(driver.title.lower())
        assert 'practical sqa' == driver.title.lower()

    def test_03(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="rememberme"]').click()
        driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
        driver.implicitly_wait(2)
        print(driver.title.lower())
        assert 'practical sqa' == driver.title.lower()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
