import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.examples.com/login")
driver.maximize_window()

time.sleep(3)
menu = driver.find_element(By.XPATH, '//*[@id="menu-item-570622"]/a/span/span')
actions = ActionChains(driver)

#1. Hover Over an Element
# actions.move_to_element(menu).perform()  # Hover over the menu
# time.sleep(5)

#2. Right-Click (Context Click)
actions.context_click(menu).perform()  # Hover over the menu
time.sleep(5)

#Drag and Drop
source = driver.find_element("id", "draggable")
target = driver.find_element("id", "droppable")
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()  # Drag the source to the target

#Double-click
element = driver.find_element("id", "double-click-area")
actions = ActionChains(driver)
actions.double_click(element).perform()  # Double-click on the element

# Click and Hold, Then Release
element = driver.find_element("id", "slider")
actions = ActionChains(driver)
actions.click_and_hold(element).move_by_offset(100, 0).release().perform()  # Drag slider by 100px
