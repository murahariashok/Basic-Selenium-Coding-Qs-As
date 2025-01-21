
'''
1.types of locators
different locators in selenium
ID
NAME
TAGNAME
CLASSNAME
LINKTEXT
PARTIALLINKTEXT
XPATH
CSS SELECTOR
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(10)

# #ID
# driver.find_element(By.ID,'email').send_keys('murahari@mail.com')
#
# #Name
# driver.find_element(By.TAG_NAME, 'email').send_keys('murahari@mail.com')

#TAGNAME
driver.find_element(By.NAME, 'email').send_keys('murahari@mail.com')
time.sleep(3)

#CLASSNAME
driver.find_element(By.CLASS_NAME, 'inputtext').send_keys('murahari@mail.com')
#LINKTEXT
driver.find_element(By.LINK_TEXT, 'Log in').click()
#PARTIALLINKTEXT
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log ').click()

#XPATH
'''
there two types of xpaths
a.absolute xpath
:using single slash / .it is a root node or document node start with html onward
/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input

b.relative xpath
:using double slash // .it is used anywhere on the document
//input[@type="text"]
'''
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys('murahari@mail.com')
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('murahari@mail.com')

#CSS SELECTOR
'''
CSS:cascade style sheet #ID .Name tagname[name='value']
'''
driver.find_element(By.CSS_SELECTOR, '#email').send_keys('murahari@mail.com')
driver.find_element(By.CSS_SELECTOR, '.email').send_keys('murahari@mail.com')
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('murahari@mail.com')






