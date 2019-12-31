def headlines(browser):
    browser.get('https://news.yahoo.com')
    headline = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a/div[3]/div/h2').text
    description = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a/div[3]/div/div/p').text
    img_src = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a/img').get_attribute('src')
    news_page = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a').get_attribute('href')

    return [headline, description, img_src, news_page]

def trending(browser):
    headlines = list()
    