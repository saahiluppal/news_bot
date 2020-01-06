import time

def fetch(browser, entities=['headlines'], count=10):

    returnable = list()

    for entity in entities:
        if entity is 'headlines': returnable.append(headlines(browser))
        if entity is 'trending': returnable.append(trending(browser, count))

    return returnable

########## Helper Functions ###########

def headlines(browser):
    browser.get('https://news.yahoo.com')

    headline_path = '/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a'
    #headline_path2= '/html/body/div/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul/li[1]/div/div/a'

    headline = browser.find_element_by_xpath(headline_path + '/div[3]/div/h2').text
    description = browser.find_element_by_xpath(headline_path + '/div[3]/div/div/p').text
    img_src = browser.find_element_by_xpath(headline_path + '/img').get_attribute('src')
    url = browser.find_element_by_xpath(headline_path).get_attribute('href')

    return [[headline], [description], [img_src], [url]]

def trending(browser, count):
    browser.get('https://news.yahoo.com')

    trending_path = '/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul'

    for val in range(2, count + 2):
        try:
            headline = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/h3/a').text
            description = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/p').text
            img_src = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[1]/div/img').get_attribute("src")
            url = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/h3/a').get_attribute('href')
            print(headline)
            print(description)
            print(img_src)
            print(url)
            print()
        except:
            pass

    return [None, None, None, None]

