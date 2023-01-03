from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")

URL = 'https://www.facebook.com/HITClub.HaUI/posts/pfbid028RrpnqZdD5KeY5sL1m6Wj3uXSBCsUy1L1MDtiRVg4cCfbKobHnHhy9f7wnyifmFhl'

browser.get(URL)

sleep(5)

# txtUesr =  browser.find_element("id" , "email")
# txtUesr.send_keys("lahuyhoang103@gmail.com")

# txtPass =  browser.find_element("id" , "pass")
# txtPass.send_keys("103202")

# txtPass.send_keys(Keys.ENTER)

# sleep(5)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(3)



cmt = browser.find_element('xpath' , '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span[1]/a')
cmt.click()

sleep(5)

all_cmt = browser.find_element( 'xpath' , '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[1]/div/div/div/div/a')
all_cmt.click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(3)

full_cmt = browser.find_element('xpath' , '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a/div')
full_cmt.click()

# sleep(5)

# full_cmt2 = browser.find_element('xpath' , '/html/body/div[1]/div[2]/div[4]/div/div/div/ul/li[3]/a')
# full_cmt2.click()

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# sleep(5)

# cmt_list = browser.find_elements('xpath', "//div[@class='_4eek _7a9b clearfix clearfix']")

# for cmt in cmt_list:
#     person = cmt.find_element( By.CLASS_NAME , '_6qw4')
#     content = cmt.find_element( By.CLASS_NAME , '_3l3x' or '_ox1')
#     print('*- ' , person.text , '-*--' , content.text)


# browser.close()