def headlines(browser):
    browser.get('https://news.yahoo.com')
    head = browser.find_element_by_xpath('//h2[@data-reactid]').text
    desc = browser.find_element_by_xpath('//p[@data-reactid]').text
    print(head)
    print(desc)
