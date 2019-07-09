import requests
import json
import time

class INDIANews:
    def __init__(self):
        url=('https://newsapi.org/v2/top-headlines?country=in&apiKey=86417ac79aea427e9d04c87169c22632')
        self.time_exceed=0
        while True:
            try:
                response = requests.get(url)
                print('Got INDIAN News.....')
                break
            except:
                print('Failed to get INDIAN news... trying again in 2 secs')
                self.time_exceed+=1
                if self.time_exceed==3:
                    print('Failed to get INDIAN News')
                    exit()
                time.sleep(2)
            
        self.jsonfile = json.loads(response.content)
    
    def getStatus(self):
        return self.jsonfile['status']

    def getJson(self):
        return json.dumps(self.jsonfile,indent=4)
    
    def getTotalResults(self):
        return self.jsonfile['totalResults']

    def getNews(self):
        self.newsFile = open("IndiaNews.txt",'w')

        for news in self.jsonfile['articles']:
            self.id = news['source']['id'] if news['source']['id']!=None else 'Unknown'
            self.name = news['source']['name'] if news['source']['name']!=None else 'Unknown'
            self.author = news['author'] if news['author']!=None else 'Unknown'
            self.title = news['title'] if news['title']!=None else 'Unknown'
            self.description = news['description'] if news['description']!=None else 'Unknown'
            self.url = news['url'] if news['url']!=None else 'Unknown'
            self.urlToImage = news['urlToImage'] if news['urlToImage']!=None else 'Unknown'
            self.publishedAt = news['publishedAt'] if news['publishedAt']!=None else 'Unknown'
            self.content = news['content'] if news['content']!=None else 'Unknown'
            self.printNews()

        self.newsFile.close()
        print('Indian News printed successful')

    def printNews(self):
        
        self.newsFile.write('Source:  ')
        self.newsFile.write('ID -- > '+self.id+'   Name --> '+self.name)
        self.newsFile.write('\nTitle: '+self.title.upper())
        self.newsFile.write('\nAuthor: '+self.author)
        self.newsFile.write('\n\nDescription:: '+self.description)
        self.newsFile.write('\n\nURL --> '+self.url)
        self.newsFile.write('\nPublished At --> '+self.publishedAt)
        self.newsFile.write('\nContent : '+self.content)
        self.newsFile.write('\n\n\n\n\n\n')
        

# For Testing Purpose
if __name__=="__main__":
    usnews = USNews()
    #print(usnews.getJson())
    usnews.getNews()
    print('INDIAN News printed Successfully')