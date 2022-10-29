import string

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
import user
from .forms import UserRegisterForm, MyForm, MyForm2
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.urls import reverse
##################################################################
####################index#######################################
from .models import Recipe
from django.shortcuts import render
from qrcode import *


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


def NewIndex(request):
    return render(request, 'user/NewIndex.html', {'title': 'index'})


########################################################################
########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            #########################mail####################################
            htmly = get_template('user/Email.html')
            d = {'username': username}
            subject, from_email, to = 'hello', 'from@example.com', 'to@emaple.com'
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'reqister here'})


###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST.get('txt_field'))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('neww')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})


def actionUrl(request):
    return render(request, 'user/navbar.html')


def neww(request):
    mainn = Recipe.objects.all()
    return render(request, 'user/neww.html', {'mainn': mainn})


def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        form.instance.rel_user = request.user
        if form.is_valid():
            form.save()
            return redirect('neww')

    else:
        form = MyForm()
    return render(request, 'user/cv-form.html', {'form': form})


def my_form_edit(request, pk):
    x = Recipe.objects.filter(id=pk)
    return render(request, 'user/my_form_edit.html', {'x': x})


def maindishes(request):
    mainn = Recipe.objects.filter(categoriesss="Main dishes")
    img_name=""
    s = len(mainn.values())
    img_name_dic = []
    for i in range(s):
        data = "http://127.0.0.1:8000/RecipePagee/" + str(mainn.values('id')[i]['id'])
        img = make(data)
        img_name = 'qr' + str(mainn.values('id')[i]['id']) + '.png'
        img_name_dic.append(img_name)
        print(img_name_dic)
        img.save(settings.MEDIA_ROOT + '/' + img_name)
    return render(request, 'user/Maindishes.html', {'mainn': mainn,"img_name_dic":img_name_dic},)


def Starters(request):
    mainn = Recipe.objects.filter(categoriesss="Starters")
    return render(request, 'user/Starters.html', {'mainn': mainn})


def Salads(request):
    mainn = Recipe.objects.filter(categoriesss="Salads")
    return render(request, 'user/Salads.html', {'mainn': mainn})


def Desserts(request):
    mainn = Recipe.objects.filter(categoriesss="Desserts")
    return render(request, 'user/Desserts.html', {'mainn': mainn})


def RecipePagee(request, pk):
    searchWord = request.POST.get('search', '')
    x = Recipe.objects.filter(id=searchWord)
    return render(request, 'user/RecipePage.html', {'x': x})


def EmailSend(request):
    if request.method == "POST":
        form = MyForm2(request.POST)
        form.instance.rel_user = request.user
        if form.is_valid():
            form.save()
    else:
        form = MyForm2()
    return render(request, {'form': form})


def My_Recipe(request):
    x = Recipe.objects.filter(author=request.user)
    return render(request, 'user/My_Recipe.html', {'x': x})


def update(request, pk):
    Recipe.objects.filter(id=pk).update(fullname=request.POST['fullname'], Time=request.POST['Time'],
                                        ResText=request.POST['ResText'], Ingredients=request.POST['Ingredients'])
    return render(request, 'user/My_Recipe.html')


def delete(request, pk):
    Recipe.objects.filter(id=pk).delete()
    return redirect('neww')
