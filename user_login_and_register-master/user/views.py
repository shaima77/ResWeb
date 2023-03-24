import string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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
from django.utils.dateparse import parse_datetime

languageVer='Hebrew'

def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


def NewIndex(request):
    global languageVer
    languageVer=request.POST.get('author')
    return render(request, 'user/NewIndex.html', {'title': 'index' ,'author':request.POST.get('author')})

def NewIndex2(request):
    return render(request, 'user/lag.html')

########################################################################
########### register here #####################################
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Profile details updated.')

            return render(request, 'user/login.html' ,{'languageVer':languageVer})
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'reqister here','author':request.POST.get('author'),'usernameDef':request.POST.get('username'),'emailDef':request.POST.get('email')})


###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('neww')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in' ,'languageVer':languageVer })


def actionUrl(request):
    return render(request, 'user/NewCv-form.html')


def neww(request):
    mainn = Recipe.objects.all()
    return render(request, 'user/neww.html', {'mainn': mainn ,'languageVer':languageVer})

@csrf_exempt
def my_form(request):
    if request.method == "POST":
        labels2 = {'fullname': "Name", "Time": "Time to Cook", "Difficulty": "Difficulty", "ResText": "Instructions"
            , "Ingredients": "Ingredients","categoriesss":"Categories","upload":"upload","author":"author"}
        labels2['fullname']=request.POST['fullname']
        labels2['Time']=request.POST['Time']
        templist=list(request.POST)
        if 'Difficulty1' in templist:
             labels2['Difficulty']='Easy'
        if 'Difficulty2' in templist:
             labels2['Difficulty']='Normal'
        if 'Difficulty3' in templist:
             labels2['Difficulty']='Hard'
        labels2['ResText']=request.POST['ResText']
        labels2['Ingredients']=request.POST['Ingredients']
        labels2['categoriesss']=request.POST['categoriesss']
        labels2['author']=request.POST['author']
        form = MyForm(labels2,request.FILES)
        form.instance.rel_user = request.user
        if form.is_valid():
            form.save()
            return redirect('neww')

    else:
        form = MyForm()
    return render(request, 'user/cv-form.html' ,{'languageVer':languageVer})

@csrf_exempt
def my_form_edit(request, pk):
    x = Recipe.objects.filter(id=pk)
    return render(request, 'user/my_form_edit.html', {'x': x ,'languageVer':languageVer})


def maindishes(request):
    mainn = Recipe.objects.filter(categoriesss="Main dishes")
    img_name=""
    s = len(mainn.values())
    img_name_dic = []
    for i in range(s):
        data = "https://cooking.pythonanywhere.com/RecipePagee/" + str(mainn.values('id')[i]['id'])
        img = make(data)
        img_name = 'qr' + str(mainn.values('id')[i]['id']) + '.png'
        img_name_dic.append(img_name)
        print(img_name_dic)
        img.save(settings.MEDIA_ROOT + '/' + img_name)
    return render(request, 'user/Maindishes.html', {'mainn': mainn,"img_name_dic":img_name_dic ,'languageVer':languageVer},)


def Starters(request):
    mainn = Recipe.objects.filter(categoriesss="Starters")
    return render(request, 'user/Starters.html', {'mainn': mainn ,'languageVer':languageVer})


def Salads(request):
    mainn = Recipe.objects.filter(categoriesss="Salads")
    return render(request, 'user/Salads.html', {'mainn': mainn ,'languageVer':languageVer})


def Desserts(request):
    mainn = Recipe.objects.filter(categoriesss="Desserts")
    return render(request, 'user/Desserts.html', {'mainn': mainn ,'languageVer':languageVer})


def RecipePagee(request, pk):
    x = Recipe.objects.filter(id=pk)
    y = x.values('Ingredients')[0]['Ingredients']
    y2 = x.values('ResText')[0]['ResText']
    t2 = y2.split(".")
    t= y.split(".")
    from langdetect import detect
    language=detect(y2)
    return render(request, 'user/RecipePage.html', {'x': x,'t':t ,'t2':t2 ,'language':language})


def EmailSend(request):
    if request.method == "POST":
        labels3={}
        labels3['name']=request.POST['name']
        labels3['date']=request.POST['date']
        labels3['Text']=request.POST['Text']
        form2 = MyForm2(labels3)
        form2.instance.rel_user = request.user
        if form2.is_valid():
            print(form2)
            form2.save()
            return redirect('neww')
    else:
        form2 = MyForm2()
    return render(request, {'form2': form2})


def My_Recipe(request):
    x = Recipe.objects.filter(author=request.user)
    return render(request, 'user/My_Recipe.html', {'x': x ,'languageVer':languageVer})

@csrf_exempt
def update(request, pk):
    Recipe.objects.filter(id=pk).update(fullname=request.POST['fullname'], Time=request.POST['Time'],
                                        ResText=request.POST['ResText'], Ingredients=request.POST['Ingredients'])
    return render(request, 'user/neww.html' ,{'languageVer':languageVer})


def delete(request, pk):
    Recipe.objects.filter(id=pk).delete()
    return redirect('neww')
