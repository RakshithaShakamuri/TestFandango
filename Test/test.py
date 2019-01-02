from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\Rakshitha Nalluri\PycharmProjects\SeleniumTest\Drivers\chromedriver.exe')

driver.set_page_load_timeout(10)
#loading the webpage
driver.get("https://www.fandango.com/")
driver.maximize_window()
time.sleep(4)
driver.get_screenshot_as_file("urltest.png")
driver.quit()