from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
class firstFBLogIn(unittest.TestCase) :
	def setUp(self) :
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.facebook.com/")

	def test_Login(self) :
		driver = self.driver
		#initialize credentials
		fbFirstName = "" #PUT YOUR FIRST NAME
		fbLastName = "" #PUT YOUR LAST NAME
		emailOrMobileNo = "" #ENTER YOUR EMAIL ID
		fbPassword = "" #ENTER YOUR PASSWORD
		birthDay = "" #ENTER YOUR DAY OF BIRTH
		birthMonth = "" #ENTER YOUR MONTH OF BIRTH
		birthYear = "" #ENTER YOUR YEAR OF BIRTH
		sex = "" #ENTER YOUR SEX

		firstNameFieldId = "u_0_1"
		lastNameFieldId = "u_0_3"
		emailOrPhoneFieldId = "u_0_5"
		emailOrPhoneConfirmationFieldId = "u_0_8"
		passwordFieldId = "u_0_a"
		birthDayFieldId = "day"
		birthMonthFieldId = "month"
		birthYearFieldId = "year"
		maleSexFieldId = "u_0_d"
		femaleSexFieldId = "u_0_e"
		singUpButtonXpath = '//button[@id="u_0_i"]'
		fbWelcomePageIconXpath = '//a[contains(@href, "logo")]'

		firstNameFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(firstNameFieldId))
		lastNameFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(lastNameFieldId))
		emailOrPhoneFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(emailOrPhoneFieldId))
		emailOrPhoneConfirmationFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(emailOrPhoneConfirmationFieldId))
		passwordFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(passwordFieldId))
		birthDayFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(birthDayFieldId))
		birthMonthFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(birthMonthFieldId))
		birthYearFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(birthYearFieldId))
		maleSexFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(maleSexFieldId))
		femaleSexFieldEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(femaleSexFieldId))
		signUpButtonEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(singUpButtonXpath))

		firstNameFieldEmerge.clear()
		firstNameFieldEmerge.send_keys(fbFirstName)
		lastNameFieldEmerge.clear()
		lastNameFieldEmerge.send_keys(fbLastName)
		emailOrPhoneFieldEmerge.clear()
		emailOrPhoneFieldEmerge.send_keys(emailOrMobileNo)
		emailOrPhoneConfirmationFieldEmerge.clear()
		emailOrPhoneConfirmationFieldEmerge.send_keys(emailOrMobileNo)
		passwordFieldEmerge.clear()
		passwordFieldEmerge.send_keys(fbPassword)
		Select(birthDayFieldEmerge).select_by_visible_text(birthDay)
		Select(birthMonthFieldEmerge).select_by_visible_text(birthMonth)
		Select(birthYearFieldEmerge).select_by_visible_text(birthYear)
		if(sex == "male") :
			maleSexFieldEmerge.click()
		else :
			femaleSexFieldEmerge.click()
		signUpButtonEmerge.click()

		fbIconEmerge = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(fbWelcomePageIconXpath))

	def tearDown(self) :
		self.driver.quit()

if __name__ == "__main__" :
	unittest.main()