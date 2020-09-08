
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver_path='/Users/tanya/Documents/chromedriver.exe'
driver=webdriver.Chrome(driver_path)
driver.get("https://web.whatsapp.com")
input("enter")
sa=driver.find_element_by_css_selector('span[title="Sahyog K18 Mech"]')
sa.click()
tinput=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
time.sleep(10)
tinput.send_keys("happy birthday")
tinput.send_keys(Keys.RETURN)
