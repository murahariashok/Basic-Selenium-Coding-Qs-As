import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)

# current_handle = driver.current_window_handle
# print(f"Current Window Handle: {current_handle}")

driver.find_element(By.XPATH,'//a[contains(text(),"OrangeHRM, Inc")]').click()
time.sleep(3)
all_handles = driver.window_handles
print(f"All Window Handles: {all_handles}")

for handle in all_handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "OrangeHRM" :
        driver.close()

time.sleep(5)
