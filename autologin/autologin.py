from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
browser.get('Website Link')
#Lets wait for lobby page to load
user = browser.find_element_by_class_name("class name") # Find the search box by class
passw = browser.find_element_by_name("name")
login = browser.find_element_by_class_name("class name") # Find the search box by class
user.send_keys("Username")
passw.send_keys("Password")
login.click()
delay = 10 # seconds max wait
browser.close()
