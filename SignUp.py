### SignUp Page Automation for a project
import time

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")
from selenium.webdriver.common.by import By


# path = "C:\Program Files (x86)\chromedriver.exe"
# driver.minimize_window()
driver.get("https://test-ambor-app-742a2.ondigitalocean.app/register")
# print(driver.current_url)

driver.find_element(By.ID, 'email').send_keys("demo@gmail.com")
driver.find_element(By.ID, 'phone').send_keys("01521503621")
driver.find_element(By.ID, 'password').send_keys("01521503621")
driver.find_element(By.ID, 'fname').send_keys("01521503621")




driver.find_element(By.ID, 'checks').click()

checkbox2 =  driver.find_element(By.ID, 'check')
checkbox2.click()

driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']").click()










driver.maximize_window()

time.sleep(6)

driver.close()

