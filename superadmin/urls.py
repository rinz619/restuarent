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

    path('userlist', views.userlist.as_view(), name='userlist'),
    path('usercreate', views.usercreate.as_view(), name='usercreate'),
    path('useredit/<int:id>', views.usercreate.as_view(), name='useredit'),
    
    path('invoicelist', views.invoicelist.as_view(), name='invoicelist'),
    path('invoicecreate', views.invoicecreate.as_view(), name='invoicecreate'),
    path('invoiceedit/<int:id>', views.invoicecreate.as_view(), name='invoiceedit'),

]