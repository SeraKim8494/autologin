from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
#from bs4 import beautifulsoup4
#import requests

driver = webdriver.Chrome('/Users/sarah/Downloads/chromedriver 8')

driver.implicitly_wait(3)

driver.get('url')

driver.find_element("xpath",'//*[@id="root"]/div/div[1]/div[1]/div[2]/button[2]').click() #로그인버튼클릭

driver.find_element("name", 'email').send_keys('sarah@redbrick.space')
driver.find_element("name", 'password').send_keys('toffjans00!')
driver.find_element("xpath", '//*[@id="popup_contents"]/div/form/button[1]').click()

driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/button[2]').click()
time.sleep(10)

driver.find_element("xpath", '//*[@id="root"]/div/section[2]/div[5]/button[1]/img').click()

elem = driver.find_element("xpath",'//*[@id="root"]/div/section[2]/div[3]/div[1]/div[2]/input')
elem.send_keys('hello')
elem.send_keys(Keys.ENTER)











