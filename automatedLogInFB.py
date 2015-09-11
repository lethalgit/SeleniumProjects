from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
class firstFBLogIn(unittest.TestCase) :
	def setUp(self) :
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.facebook.com/")

	def test_Login(self) :
		driver = self.driver
		#initialize credentials
		fbUserName = "" #PUT YOUR FB USERNAME
		fbPassWord = "" #PUT YOUR FB PASSWORD

		emailFieldId = "email"
		passFieldId = "pass"
		logInButtonXpath = '//Input[@value="Log In"]'
		fbWelcomePageIconXpath = '//a[contains(@href, "logo")]'

		emailFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(emailFieldId))
		passwordFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(passFieldId))
		logInButtonEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(logInButtonXpath))

		emailFieldEmerge.clear()
		emailFieldEmerge.send_keys(fbUserName)
		passwordFieldEmerge.clear()
		passwordFieldEmerge.send_keys(fbPassWord)
		logInButtonEmerge.click()

		fbIconEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(logInButtonXpath))

	def tearDown(self) :
		self.driver.quit()

if __name__ == "__main__" :
	unittest.main()