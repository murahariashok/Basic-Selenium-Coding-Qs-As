import time

from selenium import webdriver
driver =webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Register.html')
# driver.navigate().to('https://demo.automationtesting.in/Register.html')

driver.execute_script("window.open('https://www.bing.com', '_blank');")
driver.maximize_window()
time.sleep(3)
driver.close()
#driver.quit()