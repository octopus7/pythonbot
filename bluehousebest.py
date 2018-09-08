#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime

pypath = os.path.dirname(os.path.abspath(__file__))
print(pypath)

chromepath = 'chromedriver'

drvpath_filepath = f'{pypath}/../drvpath.txt'

htmlpath = f'{pypath}/html_bluehouse'
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
    url = f"https://www1.president.go.kr/petitions?order=best&page={page}"
    print(f"page : {page} {url}")
    browser.get(url)
    print(browser.title)
    f = open(f"{htmlpath}/{datetime_onstart}_{page}.htm", encoding='utf-8', mode = 'w')
    f.write(browser.page_source)
    f.close()

browser.quit()