from USNews import USNews
from INDIANews import INDIANews

usnews = USNews()
print("Status:",usnews.getStatus())
print("Total Results",usnews.getTotalResults())
usnews.getNews()
print('\n\n')
indianews = INDIANews()
print('Status:',indianews.getStatus())
print('Total Results:',indianews.getTotalResults())
indianews.getNews()
