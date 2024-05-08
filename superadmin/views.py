from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse,JsonResponse
from superadmin.helper import renderhelper,is_ajax
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

        return renderhelper(request, 'login', 'login',context)
    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=username, password=password)
        if user:
            login(request, user)
            return redirect('superadmin:dashboard')
        else:
            context['username'] = username
            context['password'] = password
            messages.info(request, 'Invalid Username or Password')
            return renderhelper(request, 'login', 'login',context)


class Logout(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('superadmin:login')


class dashboard(LoginRequiredMixin,View):
    def get(self, request):
        context = {}
        return renderhelper(request, 'home', 'index',context)



# Banner module start
class bannerlist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Banner.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Banner.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            if status:
                conditions &= Q(is_active=status)
            data_list = Banner.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/banner/banner-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Banner.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'banner', 'banner-view', context)

class bannercreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Banner.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'banner', 'banner-create', context)

    def post(self, request, id=None):
        try:
            data = Banner.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Banner()
            messages.info(request, 'Successfully Added')

        title = request.POST['title']
        image = request.FILES.get('imagefile')
        if image:
            file_extension = image.name.split('.')[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                type = 1
            else:
                type = 2
            data.image = image
            data.type=type

        data.title=title
        data.save()
        return redirect('superadmin:bannerlist')

    # Banner module end



# Banner module start
class gallerylist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Gallery.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Gallery.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            if status:
                conditions &= Q(is_active=status)
            data_list = Gallery.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/gallery/gallery-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Gallery.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'gallery', 'gallery-view', context)

class gallerycreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Gallery.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'gallery', 'gallery-create', context)

    def post(self, request, id=None):
        try:
            data = Gallery.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Gallery()
            messages.info(request, 'Successfully Added')


        image = request.FILES.get('imagefile')
        data.image=image
        data.save()
        return redirect('superadmin:gallerylist')

    # Banner module end



# Category module start
class categorylist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            search = request.GET.get('search')
            status = request.GET.get('status')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Category.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Category.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            if search:
                conditions &= Q(title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = Category.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/category/category-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Category.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'category', 'category-view', context)

class categorycreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Category.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'category', 'category-create', context)

    def post(self, request, id=None):
        try:
            data = Category.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Category()
            messages.info(request, 'Successfully Added')


        title = request.POST['title']
        image = request.FILES.get('image')
        icon = request.FILES.get('icon')

        if image:
            data.image=image
        if icon:
            print(icon)
            data.icon=icon
        data.title=title
        data.save()
        return redirect('superadmin:categorylist')

    # Category module end




# Category module start
class menulist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Menu.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Menu.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            if status:
                conditions &= Q(is_active=status)
            data_list = Menu.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/menu/menu-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Menu.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'menu', 'menu-view', context)

class menucreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Menu.objects.get(id=id)
        except:
            context['data'] = None

        context['category'] = Category.objects.filter(is_active=True)
        return renderhelper(request, 'menu', 'menu-create', context)

    def post(self, request, id=None):
        try:
            data = Menu.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Menu()
            messages.info(request, 'Successfully Added')


        title = request.POST['title']
        category = request.POST['category']
        cat = Category.objects.get(id=category)
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES.get('image')
        if image:
            data.image=image
        data.title=title
        data.price=price
        data.category=cat
        data.description=description
        data.save()
        return redirect('superadmin:menulist')

    # Menu module end




# Testimonial module start
class testimoniallist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            search = request.GET.get('search')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Testimonials.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Testimonials.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            if status:
                conditions &= Q(is_active=status)
            if search:
                conditions &= Q(user__icontains=search)
            data_list = Testimonials.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/testimonial/testimonial-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Testimonials.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'testimonial', 'testimonial-view', context)

class testimonialcreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Testimonials.objects.get(id=id)
        except:
            context['data'] = None

        return renderhelper(request, 'testimonial', 'testimonial-create', context)

    def post(self, request, id=None):
        try:
            data = Testimonials.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Testimonials()
            messages.info(request, 'Successfully Added')


        user = request.POST['user']
        description = request.POST['message']
        star = request.POST['star']


        data.user=user
        data.description=description
        data.star=star
        data.is_active=True
        data.save()
        return redirect('superadmin:testimoniallist')

    # Testimonial module end


class reservationlist(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()

        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Reservations.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Reservations.objects.filter(id=id).update(is_active=True)
                messages.info(request, 'Successfully Reserved')
            if status:
                conditions &= Q(is_active=status)
            data_list = Reservations.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/reservations/reservation-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Reservations.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num
        return renderhelper(request, 'reservations', 'reservation-view', context)