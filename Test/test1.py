from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\Rakshitha Nalluri\PycharmProjects\SeleniumTest\Drivers\chromedriver.exe')

driver.set_page_load_timeout(10)
driver.get("https://www.fandango.com/")
#Click on Sign in Page
driver.find_element_by_class_name("hide-logged-in").click()
driver.maximize_window()
time.sleep(4)
driver.get_screenshot_as_file("signin.png")
driver.quit()