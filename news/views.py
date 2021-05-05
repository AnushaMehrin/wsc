from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

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


# #Getting news from Dhaka Tribune 
# DhakaTribune_r = requests.get('https://www.dhakatribune.com/').text
# DhakaTribune_soup2 = BeautifulSoup(DhakaTribune_r, 'lxml')

# DhakaTribune_rep = open('newsheadlines.txt','a')
# DhakaTribune_rep.write("News headline from dhakatribune")
# DhakaTribune_rep.write("")
# DhakaTri = []
# DhakaTri1 = []
# DhakaTri2 = []
# DhakaTri.extend(DhakaTri1)
# DhakaTri.extend(DhakaTri2)

# cname : str =  "single-news-content"
# for news in DhakaTribune_soup2.find_all('div', class_ = 'single-news-content'):
#     nz =news.a.single-news-cont 
#     print(nz)
#     DhakaTribune_rep.write(nz)
#     DhakaTri.append(nz1)
# for news in DhakaTribune_soup2.find_all('div', class_ = 'report-title'):
#     nz = news.a.report-title
#     print(nz)
#     DhakaTribune_rep.write(nz)
#     DhakaTri1.append(nz)

# for news in DhakaTribune_soup2.find_all('div', class_ ='dhaka_banner-content'):
#     nz = news.a.dhaka_banner-content
#     DhakaTribune_rep.write(nz)
#     DhakaTri2.append(nz)

# DhakaTribune_rep.close()

# #Getting news from Prothom Alo
ProthomAlo_r = requests.fget('https://en.prothomalo.com/').text
ProthomAlo_soup = BeautiulSoup(ProthomAlo_r, 'lxml')
# ProthomAlo_news3 = ProthomAlo_soup.find( class_ = 'text').a.text
ProthomAlo_rep = open('newsheadlines.txt','a')
ProthomAlo_rep.write("News headline from prothmalo")
ProthomAlo_rep.write("")
Palo = [] 


for news in ProthomAlo_soup.find_all('h2',style='color:'):
    news3 = news.a.text
    print(news3)
    print()
    ProthomAlo_rep.write(news3)
    Palo.append(news3)
ProthomAlo_rep.close()


def bdNews24(req):
    name = "BDNews24.com"
    obj = BDNews24

    return render(req, 'news/index.html', {'post':obj, 'name' : name})


def dhakaTribune(req):

    name = "Dhaka Tribune"
    obj = DhakaTri
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


def prothomAlo(req):
    name = "Prothom Alo"
    obj = Palo
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


def home(request):
    txt="news" 
    return HttpResponse(txt)