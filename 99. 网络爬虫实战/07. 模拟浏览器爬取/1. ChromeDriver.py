from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.so.com')
input =browser.find_element_by_id('input')
input.send_keys('叶世立')
input.send_keys(Keys.ENTER)
