from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse,JsonResponse
from website.helper import renderhelper,is_ajax
from django.contrib.auth import login,logout, authenticate
from django.shortcuts import redirect
from superadmin.custom_permision import LoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from superadmin.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.db.models import Q
import sys





# Create your views here.
class index(View):
    def get(self, request):
        context = {}
        context['banners'] = Banner.objects.filter(is_active=True).order_by('?')[:1]
        context['gallery'] = Gallery.objects.filter(is_active=True).order_by('-id')[:6]
        context['testimonials'] = Testimonials.objects.filter(is_active=True).order_by('-id')[:6]
        category = Category.objects.filter(is_active=True).order_by('id')
        cate = menuincategory(category,many=True)
        context['category'] = cate.data
        try:
            context['popup'] = Popups.objects.get(id=1,is_active=True)
        except:
            context['popup'] =None
        return renderhelper(request, 'home', 'index',context)
    def post(self,request):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        person = request.POST['people']
        date = request.POST['date']
        time = request.POST['time']
        Reservations(name=name,phone=phone,email=email,person=person,date=date,time=time).save()
        return redirect('website:reservation')
class galleryimages(View):
    def get(self, request):
        context = {}
        context['category'] = category= Category.objects.filter(is_active=True).order_by('id')
        context['gallery'] = Gallery.objects.filter(is_active=True).order_by('-id')
        return renderhelper(request, 'gallery', 'gallery-view',context)
class menuitems(View):
    def get(self, request,item):
        context = {}
        context['category'] = category = Category.objects.filter(is_active=True).order_by('id')
        context['menu'] = Menu.objects.filter(category__title__icontains=item)
        # context['gallery'] = Gallery.objects.filter(is_active=True).order_by('-id')
        return renderhelper(request, 'menu', 'menu',context)

class contactus(View):
    def get(self, request):
        context = {}
        context['category'] = category = Category.objects.filter(is_active=True).order_by('id')
        return renderhelper(request, 'contact', 'contactus',context)
    def post(self,request):
        print('in')
        return redirect('website:contactus')

class aboutus(View):
    def get(self, request):
        context = {}
        context['category'] = category = Category.objects.filter(is_active=True).order_by('id')
        return renderhelper(request, 'about', 'about',context)


class reservation(View):
    def get(self, request):
        context = {}
        context['category'] = category = Category.objects.filter(is_active=True).order_by('id')
        return renderhelper(request, 'success', 'reservationsuccess',context)


def gotomenu(request):
    item = request.GET['item']
    return JsonResponse({'item':item})

from django.shortcuts import render

def error_404(request, exception):
    return render(request, '404.html', status=404)