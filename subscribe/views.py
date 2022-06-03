from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import subs_page
from .models import Subscribe, Contact_Us
import requests


def subscribe(request):
    sub = subs_page(request.POST or None)
    if sub.is_valid():
        check_num = list(Subscribe.objects.values('phone'))
        form_num = int(request.POST.get("phone", ""))
        for i in check_num:
            c = i
            for key, values in c.items():
                if form_num == values:
                    return HttpResponse("A account is already registered by this number ")
        sub.save()
        return render(request, 'Subscribe/Thanks.html')

    context = {
        "form": sub
    }
    return render(request, 'Subscribe/Subs_Form.html', context)

def  Construct_SMS(request):
    sent_to = list(Subscribe.objects.values('name', 'phone', 'email', 'headlines', 'bussiness', 'entertainment', 'health', 'science', 'technology', 'sports'))
    for i in sent_to:
        News_Matter = {}
        coustomer = i
        print(coustomer['name'])
        if coustomer['headlines'] == True:
            name = coustomer['name']
            starting_message = "Good Morning {} Here Are Some Today's Updates".format(name)
            phone = coustomer['phone']
            r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=43a3a6d4d9204f8886265212e5cc2f97')
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Headlines"] = news_content
        if coustomer['bussiness']==True:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Bussiness"] = news_content
        if coustomer['entertainment']==True:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Technology"] = news_content
        if coustomer['health']==True:
            r = requests.get
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Health"] = news_content
        if coustomer['science']==True:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Science"] = news_content
        if coustomer['technology']==True:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Technology"] = news_content
        if coustomer['sports']==True:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=43a3a6d4d9204f8886265212e5cc2f97")
            a = 0
            news_content = {}
            news = r.json()
            o = (news["articles"])
            for i in o:
                news_title = (i["title"])
                news_desc = (i["description"])
                news_url = (i["url"])
                a += 1
                news_content[a] = {}
                news_content[a]['title'] = news_title
                news_content[a]['desc'] = news_desc
                news_content[a]['url'] = news_url
            News_Matter["Spots"] = news_content
        return JsonResponse(News_Matter,safe=False)

def Contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact_Us(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return HttpResponse("Your query has been submitted...we will answer as soon as possible...""<a href='/home'><button type='button' class='btn btn-primary'>Back To Home</button></a>")
    return render(request, 'News/Contact_us.html')


