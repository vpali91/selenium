from selenium import webdriver
from selenium.webdriver.common.by import By
import time

all_addresses = ['Bekescsaba', 'Szeged', 'Budapest']
all_prices = ['60000', '80000', '100000']
all_links = ['fdhdhjdfhd', 'jgfjfgjfggjfj', 'eeeeeeeeeeeeee']


# Create Spreadsheet using Google Form
# Substitute your own path here 👇
chrome_driver_path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_addresses)):
    # Substitute your own Google Form URL here 👇
    driver.get('https://forms.gle/qQ3PC2NTMo1MYaPn9')

    time.sleep(2)
    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
