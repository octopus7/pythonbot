#-*- coding: utf-8 -*-

import os
import datetime
import telegram
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pypath = os.path.dirname(os.path.abspath(__file__))
print(pypath)

id = ""
password = ""
account_path = f'{pypath}/../interpark.txt'
with open(account_path, 'r') as myfile:
    id = myfile.readline().rstrip()
    password = myfile.readline()

#print (id)
#print (password)

my_token = "telegramtoken"
my_userid = 0
telegram_path = f'{pypath}/../telegram.txt'
with open(telegram_path, 'r') as myfile:
    my_token = myfile.readline().rstrip()
    my_userid = myfile.readline()

chromepath = 'chromedriver'
drvpath_filepath = f'{pypath}/../drvpath.txt'

if not  os.path.isfile(drvpath_filepath):
    print(drvpath_filepath + " not found!")
    quit();

with open(drvpath_filepath, 'r') as myfile:
    chromepath = myfile.read()

options = Options()
#options.add_argument('--headless')
browser = webdriver.Chrome(chromepath, chrome_options=options)
browser.get("https://m.interpark.com/auth/login.html")
print(browser.title)

browser.find_element_by_name("userId").send_keys(id)
browser.find_element_by_name("userPwd").send_keys(password)
browser.find_element_by_id("btn_login").click()

browser.get("http://ipointmall.interpark.com/ipoint/MyIpointDtl.do?_method=initialMobile")

#browser.find_element_by_xpath("//*[@id=\"wrap\"]/div[2]/div[2]/div[1]/nav/ul/li[2]/a").click()
# browser.execute("javascript:fnSetSearchType('1');fnGetPointList(1, '', '1');return false;")
browser.implicitly_wait(1)

point = "Interpark " +  datetime.datetime.now().strftime("%Y-%m-%d")
point += "\n" + browser.find_element_by_id("usableAmt").text
lines = browser.find_element_by_id("conts01").text.splitlines()
for lidx in range(0,6):
    now = "\n" + lines[lidx*4+0] + str(lines[lidx*4+1])[5:] + lines[lidx*4+2]
    now = now.replace("적립","")
    point += now;
systemver = sys.version

print (point)

browser.implicitly_wait(1)

bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id = my_userid, text= point) 

browser.quit()
