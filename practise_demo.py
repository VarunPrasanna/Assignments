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

driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

plot = len(driver.find_elements(By.XPATH,"(//span[@class='price']/preceding::h3)"))

for i in range(1,plot+1):
    flat = driver.find_element(By.XPATH,"(//span[@class='price']/preceding::h3)["+str(i)+"]").text
    print(flat)
