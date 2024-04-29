from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from website import views
from django.conf.urls import handler404

app_name = 'website'

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('galleryimages',views.galleryimages.as_view(),name='galleryimages'),
    path('contactus',views.contactus.as_view(),name='contactus'),
    path('menuitems/<str:item>',views.menuitems.as_view(),name='menuitems'),
    path('gotomenu',views.gotomenu,name='gotomenu'),

]

handler404 = views.error_404