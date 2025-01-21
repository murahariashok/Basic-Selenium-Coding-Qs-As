import time

from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()
time.sleep(5)
driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)

#back()
driver.back()
time.sleep(5)

#forward()
driver.forward()
time.sleep(5)

#refresh()
driver.refresh()
time.sleep(5)