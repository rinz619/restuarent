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
        category = Category.objects.filter(is_active=True).order_by('id')
        cate = menuincategory(category,many=True)
        context['category'] = cate.data
        return renderhelper(request, 'home', 'index',context)