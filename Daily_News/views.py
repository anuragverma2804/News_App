from django.shortcuts import render
import requests

def first_page(request):
    return render(request, 'News/First_Page.html')
    

    
def home_page(request):
    return render(request,'News/Home.html')


def today_headlines(request):
    r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=43a3a6d4d9204f8886265212e5cc2f97')
    news = r.json()
    o = (news["articles"])
    news_content={}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Todays_headlines.html', {"news":news_content})

def bussiness(request):
    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Bussiness.html', {"news": news_content})
def entertainment(request):
    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Entertainment.html', {"news": news_content})

def science(request):

    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Science.html', {"news": news_content})

def health(request):

    r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=43a3a6d4d9204f8886265212e5cc2f97')
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Health.html', {"news": news_content})

def technology(request):

    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Technology.html', {"news": news_content})

def sport(request):

    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
    news = r.json()
    o = (news["articles"])
    news_content = {}
    a = 0
    for i in o:
        news_str = (i["title"])
        desc_str = (i["description"])
        url_str = (i["url"])
        publishedAt_str = (i["publishedAt"])
        a += 1
        news_content[a] = {}
        news_content[a]['title'] = news_str
        news_content[a]['desc'] = desc_str
        news_content[a]['url'] = url_str
        news_content[a]['publishedAt'] = publishedAt_str
    return render(request, 'News/Sport.html', {"news": news_content})



def About_us(request):
    return render(request,'News/About_us.html')


