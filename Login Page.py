from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

phone = "01521503628"
password = "demo1234"

url = "https://test-ambor-app-742a2.ondigitalocean.app/login"

# path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")

driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "phone_number").send_keys(phone)
sleep(1)

driver.find_element(By.ID, "password").send_keys(password)
sleep(2)

driver.find_element(By.CLASS_NAME, "submit_btn").click()
sleep(3)

print('Test Successful')

driver.quit()

