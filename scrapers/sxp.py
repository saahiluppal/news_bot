from selenium import webdriver
import yahoo_sxp as yahoo
import os
import time

browser = webdriver.Firefox(executable_path=os.getcwd()+'/geckodriver')
#yahoo.headlines(browser)
yahoo.trending(browser)
browser.close()
