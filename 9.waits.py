import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.examples.com/login")
driver.maximize_window()

# driver.implicitly_wait(10)
# time.sleep(3)
# menu = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()

wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Home')]")))
element.click()