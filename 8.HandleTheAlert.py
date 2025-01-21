import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Alerts.html')
# driver.navigate().to('https://demo.automationtesting.in/Register.html')
driver.maximize_window()
time.sleep(3)


#//a[@class="analystic"]
#//a[@href="#CancelTab"]
#//a[@href="#Textbox"]
#//button[@onclick="alertbox()"]
driver.find_element(By.XPATH,'//a[@class="analystic"]').click()
driver.find_element(By.XPATH,'//button[@onclick="alertbox()"]').click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

#//a[@href="#CancelTab"]
#//button[@onclick="confirmbox()"]
driver.find_element(By.XPATH,'//a[@href="#CancelTab"]').click()
driver.find_element(By.XPATH,'//button[@onclick="confirmbox()"]').click()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)

#//a[@href="#Textbox"]
#//button[@onclick="promptbox()"]
driver.find_element(By.XPATH,'//a[@href="#Textbox"]').click()
driver.find_element(By.XPATH,'//button[@onclick="promptbox()"]').click()
alert = driver.switch_to.alert
alert.send_keys("")
time.sleep(2)
alert.send_keys('ashok kumar')
alert.accept()
time.sleep(3)
