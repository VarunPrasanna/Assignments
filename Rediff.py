import time
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.options import BaseOptions


serv_obj = Service("C:/Users/varun/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(7)

driver.get("https://register.rediff.com/register/register.php?FormName=user_details") # to open the URL
driver.maximize_window() # To maximise the window

driver.find_element(By.XPATH,"//td[text()='Full Name']/following-sibling::td[2]/input").send_keys("Varun Prasanna") #Following sibling xpath

driver.find_element(By.XPATH,"//td[text()='Choose a Rediffmail ID']/following-sibling::td[2]/input[1]").send_keys("varun prasanna") ##Following sibling xpath

driver.find_element(By.ID,"newpasswd").send_keys("V@rUN")
driver.find_element(By.XPATH,"//td[text()='Password']/following-sibling::td[2]/em").click() # To click the hide password #Following sibling xpath
driver.find_element(By.XPATH,"//td[text()='Retype password']/following-sibling::td[2]/input").send_keys("V@rUN") #Following sibling xpath
driver.find_element(By.XPATH,"//td[text()='Alternate Email Address']/following-sibling::td[2]/input").send_keys("Nuravhsa@gmail.com") #Following sibling xpath
driver.find_element(By.ID,"mobno").send_keys("9876543210") # Mobile no

# Select class
Day=driver.find_element(By.XPATH,"//td[text()='Date of Birth']/following-sibling::td[2]/select")
Day = Select(Day).select_by_visible_text("16") # Day ...... By visible Text

Month = driver.find_element(By.XPATH,"//td[text()='Date of Birth']/following-sibling::td[2]/select[2]")
Month = Select(Month).select_by_visible_text("MAR")  # Month ...... By visible Text

Year = driver.find_element(By.XPATH,"//td[text()='Date of Birth']/following-sibling::td[2]/select[3]")
Year = Select(Year).select_by_visible_text("2022")  # Year ........by visible text

driver.find_element(By.XPATH,"//td[text()='Gender']/following-sibling::td[2]").click() # To click male


country = driver.find_element(By.XPATH,"//span[text()='Country']/following::td[2]/select")
country = Select(country).select_by_visible_text("Australia")

driver.find_element(By.ID,"Register").click()
driver.switch_to.alert.accept()  # To accept the pop up
print(driver.title)

time.sleep(4)
driver.close()



