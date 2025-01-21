import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Register.html')
# driver.navigate().to('https://demo.automationtesting.in/Register.html')
driver.maximize_window()
time.sleep(3)

# store = driver.find_element(By.ID,"Skills").text
store = driver.find_elements(By.XPATH,'//select[@id="Skills"]/option')

list = []
for i in store:
    list.append(i.text)
    # print(i.text) #return the all skills
    # print(i) #idsession
print(list)


