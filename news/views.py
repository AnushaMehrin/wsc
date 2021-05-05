from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests, csv

#Getting news from BdNews24
BDNews24_r = requests.get('https://bdnews24.com/').text
BDNews24_soup2 = BeautifulSoup(BDNews24_r, 'lxml')

BDNews24_rep = open('newsheadlines.txt','a')
BDNews24_rep.write("News headline from bdnews24")
BDNews24_rep.write("")
BDNews24 = []
for news in BDNews24_soup2.find_all('div', class_ = 'text'):
    BDNews24_headline =news.a.text
    BDNews24_rep.write(BDNews24_headline)
    print(BDNews24_headline)
    BDNews24.append(BDNews24_headline)
    print()
BDNews24_rep.close()


#Getting news from Prothom Alo
# ProthomAlo_r = requests.get('https://en.prothomalo.com/').text
# ProthomAlo_soup = BeautiulSoup(ProthomAlo_r, 'lxml')
# # ProthomAlo_news3 = ProthomAlo_soup.find( class_ = 'text').a.text
# ProthomAlo_rep = open('newsheadlines.txt','a')
# ProthomAlo_rep.write("News headline from prothmalo")
# ProthomAlo_rep.write("")

prothomAlo_URL = "https://en.prothomalo.com/"
prothomAlo_r = requests.get(prothomAlo_URL)
prothomAlo_soup = BeautifulSoup(prothomAlo_r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
Palo = [] 

main = prothomAlo_soup.find('div', attrs = {'class' : 'fourteenStories3Ad1Widget-m__wrapper__14yBW'})
h2 = prothomAlo_soup.find('div', attrs = {'class' : 'headline-title newsHeadline-m__title__2_I3j newsHeadline-m__bigSize__2doEw'})

for news in prothomAlo_soup.find_all('a', attrs = {'class' :'newsHeadline-m__title-link__1puEG'}):
    news = news.text
    print(news)
    print()
    Palo.append(news)



tds_URL = "https://www.thedailystar.net/bangla/"
tds_r = requests.get(tds_URL)
tds_soup = BeautifulSoup(tds_r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
tds_news = []

for news in tds_soup.findAll('div', attrs = {'class':'highlight-text'}) :

    news = news.h1.text
    print(news)
    print()
    tds_news.append(news)


morehighlight = tds_soup.find('div', attrs = {'class':'more-highlight'})

for news in morehighlight.findAll('div', attrs = {'class':'two-50'}) :
    
    news = news.h3.text
    print(news)
    print()
    tds_news.append(news)

for news in morehighlight.findAll('div', attrs = {'class':'three-33 margin-bottom-zero'}) :
    
    news = news.h4.text
    print(news)
    print()
    tds_news.append(news)


# leftside = tds_soup.find('h5', attrs = {'class':'list-border'})
for news in tds_soup.findAll('h5') :
    
    news = news.a.text
    print(news)
    print()
    tds_news.append(news)


dt_URL = "https://bangla.dhakatribune.com/"
dt_r = requests.get(dt_URL)
dt_soup = BeautifulSoup(dt_r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
dt_news = []

singlenews = dt_soup.find( 'ul', attrs = {'class': 'just_in_news'} )
for news in dt_soup.findAll( 'div', attrs = {'class': 'dt-strem-cont'}) :
    
    news = news.h2.text
    print(news)
    print()
    dt_news.append(news)



def bdNews24(req):
    name = "BDNews24.com"
    obj = BDNews24

    return render(req, 'news/index.html', {'post':obj, 'name' : name})


def theDailyStar(req):

    name = "The Daily Star"
    obj = tds_news
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})

def prothomAlo(req):
    name = "Prothom Alo"
    obj = Palo
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


def dhakaTribune(req):

    name = "Dhaka Tribune"
    obj = dt_news
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


def home(request):
    txt = "news" 
    return HttpResponse(txt)