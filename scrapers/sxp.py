from selenium import webdriver
import yahoo_sxp as yahoo
import os

browser = webdriver.Firefox(executable_path=os.getcwd()+'/geckodriver')
print(yahoo.fetch(browser, ['trending']))
#browser.close()
