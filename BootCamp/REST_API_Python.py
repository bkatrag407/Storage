import requests

r=requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-4-11&to=2022-4-12&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
print(type(r))
output=r.json()
print(type(output))
#print(output['articles'])
articles = output['articles']
#print(articles)

for article in articles:
    print(article['title'])
