from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page,name=''),
    path('home', views.home_page,name=''),
    path('subscribe', include('subscribe.urls')),
    path('todays_headlines',views.today_headlines,name=''),
    path('bussiness',views.bussiness,name=''),
    path('entertainment',views.entertainment,name=''),
    path('science',views.science,name=''),
    path('health',views.health,name=''),
    path('technology',views.technology,name=''),
    path('sport',views.sport,name=''),
    path('About_us',views.About_us,name=''),

]
