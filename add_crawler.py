import json

crawl = {
    'yahoo': {
        "highlights": "https://news.yahoo.com/",
        "world": "https://news.yahoo.com/world/",
        "politics": "https://news.yahoo.com/politics/",
        "business": "",
        "entertainment": "",
        "health": "https://news.yahoo.com/health/",
        "science": "https://news.yahoo.com/science/",
        "search": "",
    },
    'huffpost': {
        "highlights": "https://www.huffpost.com/news/",
        "world": "https://www.huffpost.com/news/world-news",
        "politics": "https://www.huffpost.com/news/politics",
        "business": "",
        "entertainment": "https://www.huffpost.com/entertainment/",
        "health": "",
        "science": "",
        "search": "",
    },
    'cnn': {
        "highlights": "https://edition.cnn.com/",
        "world": "https://edition.cnn.com/world",
        "politics": "https://edition.cnn.com/politics",
        "business": "https://edition.cnn.com/business",
        "entertainment": "https://edition.cnn.com/entertainment",
        "health": "https://edition.cnn.com/health",
        "science": "",
        "search": "",
    },
    'nytimes': {
        "highlights": "https://www.nytimes.com/",
    },
    'foxnews': {
        "highlights": "https://www.foxnews.com/",
    },
    "nbcnews": {
        "highlights": "https://www.nbcnews.com/",
    },
    "bbcnews": {
        "highlights": "https://www.bbc.com/news",
    },
    "abcnews": {
        "highlights": "https://abcnews.go.com/"
    }
}

with open('crawl.json','w') as outfile:
    json.dump(crawl, outfile,indent=4)
