#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime

pypath = os.path.dirname(os.path.abspath(__file__))
print(pypath)

chromepath = 'chromedriver'

drvpath_filepath = pypath +'/../drvpath.txt'

htmlpath = pypath +'/html_bluehouse'
if not os.path.exists(htmlpath):
    os.makedirs(htmlpath)

if not  os.path.isfile(drvpath_filepath):
    print(drvpath_filepath + " not found!")
    quit();

with open(drvpath_filepath, 'r') as myfile:
    chromepath = myfile.read()

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chromepath, chrome_options=options)

datetime_onstart  =datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

for page in range(1,4):
    print("page : " + str(page))
    browser.get("https://www1.president.go.kr/petitions?order=best&page=" + str(page))
    print(browser.title)
    f = open(htmlpath+"/" + datetime_onstart +"_"+str(page) +".htm", encoding='utf-8', mode = 'w')
    f.write(browser.page_source)
    f.close()

browser.quit()