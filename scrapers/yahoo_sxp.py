def fetch(browser, entities=['headlines'], count=10):

    returnable = list()

    for entity in entities:
        if entity is 'headlines': returnable.append(headlines(browser))
        if entity is 'trending': returnable.append(trending(browser, 5))
        if entity is 'world': returnable.append(world(browser, count))

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

    print('Implement it again')

    trending_path = '/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul'
    browser.implicitly_wait(1)

    for val in range(2, count + 2):
        try:
            headline = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/h3/a').text
            description = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/p').text
            img_src = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[1]/div/img').get_attribute("src")
            url = browser.find_element_by_xpath(trending_path + f'/li[{val}]/div/div/div[2]/h3/a').get_attribute('href')
        except:
            pass

    return [None, None, None, None]

def world(browser, count):
    browser.get('https://news.yahoo.com/world/')

    path = '/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/ul'
    headlines = []
    descriptions = []
    img_srcs = []
    urls = []
    counter = 0

    for i in range(100):
        try:
            headline = browser.find_element_by_xpath(path + f'/li[{i}]/div/div/div[2]/h3/a').text
            description = browser.find_element_by_xpath(path + f'/li[{i}]/div/div/div[2]/p').text
            img_src = browser.find_element_by_xpath(path + f'/li[{i}]/div/div/div[1]/div/img').get_attribute('src')
            url = browser.find_element_by_xpath(path + f'/li[{i}]/div/div/div[2]/h3/a').get_attribute('href')
            print(url)
            headlines.append(headline)
            descriptions.append(description)
            img_srcs.append(img_src)
            url.append(url)
            counter+=1
            if counter >= count:
                break
        except:
            pass

        print(headlines, descriptions, img_srcs, urls)
        return [headlines, descriptions, img_srcs, urls]