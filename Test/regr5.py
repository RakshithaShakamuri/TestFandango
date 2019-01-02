from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\Rakshitha Nalluri\PycharmProjects\SeleniumTest\Drivers\chromedriver.exe')

driver.set_page_load_timeout(10)
driver.get("https://www.fandango.com/")
driver.maximize_window()
driver.find_element_by_class_name("page-header-emphasis").click()
driver.find_element_by_id("FirstNameBox").send_keys("national")
driver.find_element_by_id("EmailAddressBox").send_keys("national.university123@gmail.com")
driver.find_element_by_id(("PasswordBox")).send_keys("National@123")
driver.find_element_by_id(("ConfirmPasswordBox")).send_keys("")
driver.find_element_by_id("ctl00_GlobalBody_VipRegistration_JoinNowButton").click()
time.sleep(4)
# driver.get_screenshot_as_file("rule6.png")
driver.quit()