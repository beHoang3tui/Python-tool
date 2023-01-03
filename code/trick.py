from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")



browser.get("https://forms.gle/bFBM4apzGhCb6sBN8")
txtUesr =  browser.find_element('xpath' , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
txtUesr.send_keys("chocon2k4")

txtUesr1 =  browser.find_element('xpath' , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
txtUesr1.send_keys("203099999999999999999999999")

step2 = browser.find_element('xpath' , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label')
step2.click()

step3 = browser.find_element('xpath' , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/label')
step3.click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

step4 = browser.find_element('xpath' , '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
step4.click()

browser.close()