from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

x = input("Tweet Now :")
chromePath = r'''C:\Users\hp\Desktop\chromedriver_win32 (1)\chromedriver'''
driver = webdriver.Chrome(executable_path=chromePath)
driver.get('https://twitter.com/login')
sleep(2)
driver.maximize_window()
sleep(3)
email = driver.find_element_by_name('session[username_or_email]')
email.send_keys("username_or_email__your_twitter_account") #username or email
sleep(3)
password = driver.find_element_by_name('session[password]')
password.send_keys("password__your_twitter_account") #password
sleep(3)
ent = driver.find_element_by_name("session[password]")
ent.send_keys(u'\ue007')
sleep(4)
add = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
add.send_keys(x)
add.send_keys(u'\ue007')
sleep(2)
mouse_key = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span").click()
