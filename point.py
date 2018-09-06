import datetime
import telegram
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)
browser.get("https://m.interpark.com/auth/login.html")
print(browser.title)



browser.find_element_by_name("userId").send_keys("id")
browser.find_element_by_name("userPwd").send_keys("pw")
browser.find_element_by_id("btn_login").click()

browser.get("https://smshop.interpark.com/my/shop/index.html?mwm1=common&mwm2=header&mwm3=my")

point = "Interpark " + browser.find_element_by_id("mem_ipoint").text + " from pi"
systemver = sys.version

print (point)

browser.implicitly_wait(1)

my_token = "telegramtoken"
my_userid = 0
bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id = my_userid, text= point) 

browser.quit()
