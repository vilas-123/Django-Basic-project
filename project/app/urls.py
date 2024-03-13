
from django.urls import path
from app import views

urlpatterns = [
    path('search',views.search,name='search'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleblog,name='handleblog'),
    path('service',views.service,name='service'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
  
    

]
