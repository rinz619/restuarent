from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from superadmin import views
from .views import Createdatas,Listdatas
app_name = 'superadmin'

urlpatterns = [

    # Rework urls start 
    path('create/<str:form_type>/', Createdatas.as_view(), name='create'),
    path('list/<str:form_type>/', Listdatas.as_view(), name='list'),
    path('edit/<str:form_type>/<int:pk>/', views.edit, name='edit'),

     # Rework urls end 





    path('',views.index.as_view(),name='login'),
    path('Dashboard',views.dashboard.as_view(),name='dashboard'),
    path('Logout', views.Logout.as_view(), name='Logout'),

    path('bannerlist', views.bannerlist.as_view(), name='bannerlist'),
    path('bannercreate', views.bannercreate.as_view(), name='bannercreate'),
    path('banneredit/<int:id>', views.bannercreate.as_view(), name='banneredit'),

    path('categorylist', views.categorylist.as_view(), name='categorylist'),
    path('categorycreate', views.categorycreate.as_view(), name='categorycreate'),
    path('categoryedit/<int:id>', views.categorycreate.as_view(), name='categoryedit'),

    path('menulist', views.menulist.as_view(), name='menulist'),
    path('menucreate', views.menucreate.as_view(), name='menucreate'),
    path('menuedit/<int:id>', views.menucreate.as_view(), name='menuedit'),

    path('testimoniallist', views.testimoniallist.as_view(), name='testimoniallist'),
    path('testimonialcreate', views.testimonialcreate.as_view(), name='testimonialcreate'),
    path('testimonialedit/<int:id>', views.testimonialcreate.as_view(), name='testimonialedit'),



]