import time
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:/Users/varun/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(7)

driver.get("https://www.saucedemo.com/inventory.html")
driver.maximize_window()
print(driver.title)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

list = len(driver.find_elements(By.XPATH,"//div[@class='inventory_item_name']"))

# To capture all the items names in console
for i in range(1,list+1):
    box=driver.find_element(By.XPATH,"(//div[@class='inventory_item_name'])["+str(i)+"]").text  # Index Xpath
    print(box)



