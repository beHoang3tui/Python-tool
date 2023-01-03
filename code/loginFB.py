from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")


browser.get("http://facebook.com")


txtUesr =  browser.find_element("id" , "email")
txtUesr.send_keys("lahuyhoang103@gmail.com")

txtPass =  browser.find_element("id" , "pass")
txtPass.send_keys("103202")

txtPass.send_keys(Keys.ENTER)

sleep(5)

browser.close()