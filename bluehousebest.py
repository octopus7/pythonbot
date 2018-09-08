from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#pypath = os.path.dirname(os.path.abspath(__file__))

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver', chrome_options=options)

for page in range(1,4):
    print("page : " + str(page))
    browser.get("https://www1.president.go.kr/petitions?order=best&page=" + str(page))
    print(browser.title)

browser.quit()




