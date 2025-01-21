
'''
Used to interact with the drop-down menu we must import select calls
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()
time.sleep(3)

element = driver.find_element(By.XPATH,'//select[@id="country"]')
drop = Select(element)

#select_by_visible_text
# drop.select_by_visible_text("Canada")

#select_by_index
# drop.select_by_index(10)
# drop.select_by_value("BM")

#count th number of countries
# print(len(drop.options))

# for i in drop.options:
#     print(i.text) #all countries

for i in drop.options:
    if i.text == 'Zimbabwe' :
        i.click()
time.sleep(5)