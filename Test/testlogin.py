from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\Rakshitha Nalluri\PycharmProjects\SeleniumTest\Drivers\chromedriver.exe')

def rule1():
    # driver.set_page_load_timeout(10)
    driver.get("https://www.fandango.com/")
    driver.find_element_by_class_name("hide-logged-in").click()
    driver.maximize_window()
    driver.find_element_by_id("UsernameBox").send_keys("")
    driver.find_element_by_id(("PasswordBox")).send_keys("")
    driver.find_element_by_id("ctl00_GlobalBody_SignOnControl_SignInButton").click()
    time.sleep(4)
    # driver.get_screenshot_as_file("rule1.png")
    driver.quit()
    print("Rule1 successful")


def rule2():
    # driver.set_page_load_timeout(10)
    driver.get("https://www.fandango.com/")
    driver.find_element_by_class_name("hide-logged-in").click()
    driver.maximize_window()
    driver.find_element_by_id("UsernameBox").send_keys("")
    driver.find_element_by_id(("PasswordBox")).send_keys("National@123")
    # driver.find_element_by_id(("PasswordBox")).send_keys("National")
    # driver.find_element_by_id(("PasswordBox")).send_keys("")
    driver.find_element_by_id("ctl00_GlobalBody_SignOnControl_SignInButton").click()
    time.sleep(4)
    # driver.get_screenshot_as_file("rule2.png")
    driver.quit()
    print("successful rule2")

rule1()
rule2()