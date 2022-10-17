from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import UserRegisterForm, MyForm

##################################################################
####################index#######################################
from .models import Recipe


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})


def actionUrl(request):
    return render(request, 'user/navbar.html')


def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        form.instance.rel_user = request.user
        if form.is_valid():
            form.save()
            return redirect('actionUrl')

    else:
        form = MyForm()
    return render(request, 'user/cv-form.html', {'form': form})

def maindishes(request):
    mainn = Recipe.objects.filter(categoriesss="Main dishes")
    return render(request, 'user/Maindishes.html', {'mainn': mainn})


def RecipePagee(request):
    x = Recipe.objects.filter(id=18).values_list('Ingredients' ,flat=True).distinct()
    return render(request, 'user/RecipePage.html', {'x': x})
