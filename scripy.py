from selenium import webdriver
from time import sleep
from colored import fg, bg, attr
import sys
sys.stdout.write("\x1b]2; Facebook Auto Followers [ Github : rootxnova ] \x07")
color1 = fg('#0984e3')
color2 = fg('#EA2027')
color3 = fg('#ecf0f1')
print(color1+'''
    _____   ____    _____    ___    _       _        ___   __        __
   |  ___| | __ )  |  ___|  / _ \  | |     | |      / _ \  \ \      / /
   | |_    |  _ \  | |_    | | | | | |     | |     | | | |  \ \ /\ / / 
   |  _|   | |_) | |  _|   | |_| | | |___  | |___  | |_| |   \ V  V /  
   |_|     |____/  |_|      \___/  |_____| |_____|  \___/     \_/\_/   
                                                                     
   
   ====================================================================
   ==>         F A C E B O O K A U T O F O L L O W E R S            <==
   ====================================================================
   ==>          THIS TOOL CODED BY ABDELRAHMAN ABOULDAHAB"          <==
   ==>                FOLLOW ME ON GITHUB : ROOTXNOVA               <==
   ====================================================================
   ==>         F A C E B O O K A U T O F O L L O W E R S            <==
   ====================================================================

''')
order = input(color3+'   Enter File Name Or Path : ')
unametarget = input(color3+'   Enter Target Username Only : ')
driver = webdriver.Chrome()
driver.implicitly_wait(1)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com/login')
########################################### [ W O R K A R E A ] ###########################################
username = ''
password = ''
file = open(order,'r')
file = file.read().split("\n")
for i in file:
    a = i.split(':')
    username = a[0]
    password = a[1]
    email = driver.find_element_by_xpath('//*[@id="email"]').click()
    email = driver.find_element_by_xpath('//*[@id="email"]')
    passw = driver.find_element_by_xpath('//*[@id="pass"]').click()
    passw = driver.find_element_by_xpath('//*[@id="pass"]')
    email.send_keys(username)
    passw.send_keys(password)
    login = driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    sleep(5)
    driver.get('https://www.facebook.com/'+unametarget+'/')
    follow = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div[1]/a').click()
    driver.quit()
########################################### [ W O R K A R E A ] ###########################################
close = input(color2+'   Press Enter To Close Script')
