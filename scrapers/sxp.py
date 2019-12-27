from selenium import webdriver
import yahoo_sxp as yahoo
import os
import time

browser = webdriver.Firefox(executable_path=os.getcwd()+'/geckodriver')
#browser.get('https://news.yahoo.com')
#browser.get('https://www.huffpost.com/news/')
yahoo.headlines(browser)
browser.close()
