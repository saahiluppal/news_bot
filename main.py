from USNews import USNews

usnews = USNews()
print("Status",usnews.getStatus())
print("Total Results",usnews.getTotalResults())
usnews.getNews()
