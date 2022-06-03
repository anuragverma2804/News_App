from django.urls import path
from . import views
from . import admin





urlpatterns = [
    path('',views.subscribe,name=''),
    path('/abs',views.Construct_SMS,name=''),
    path('/Contact_us', views.Contact_us, name=''),

]