from selenium import webdriver

def start_chrome ():
  driver = webdriver.Chrome()
  driver.start_client()
  return driver

start_chrome()