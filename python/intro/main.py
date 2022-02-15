from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://google.com")
driver.maximize_window()
driver.get_screenshot_as_file("D:\screenshot1.png")

driver.get("https://facebook.com")
driver.get_screenshot_as_file("D:\screenshot2.png")

driver.get("https://bing.com")
inputElement = driver.find_element_by_id("sb_form_q")
driver.get_screenshot_as_file("D:\screenshot3.png")
inputElement.send_keys("some text")
inputElement.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("D:\screenshot4.png")

driver.get("https://www.tests.com/login")
driver.get_screenshot_as_file("D:\screenshot4.png")
inputElement2 = driver.find_element_by_name("em")
inputElement2.send_keys("asd")

inputElement3 = driver.find_element_by_name("pw")
inputElement3.send_keys("asdadDDA")
driver.get_screenshot_as_file("D:\screenshot5.png")
inputElement4 = driver.find_element_by_name("Login")
inputElement4.click()
driver.get_screenshot_as_file("D:\screenshot6.png")
