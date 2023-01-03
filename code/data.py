from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")

URL = 'https://classroom.google.com/c/MzczNjMyODAyNDI3/a/Mzc0NzcwODY1MzAy/submissions/by-status/and-sort-last-name/all'

browser.get(URL)
sleep(5)

txtUesr =  browser.find_element("id" , "identifierId")
txtUesr.send_keys("lahuyhoang103@gmail.com")

cmt = browser.find_elements(By.CLASS_NAME ,  'dWdaJc udxSmc')
print(cmt)

