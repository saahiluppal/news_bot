import json

crawl = {
    'yahoo': {
        "highlights": "https://news.yahoo.com/",
    },
    'huffpost': {
        "highlights": "https://www.huffpost.com/",
    },
    'cnn': {
        "highlights": "https://edition.cnn.com/",
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
