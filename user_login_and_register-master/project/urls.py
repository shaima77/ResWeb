"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth

from .router import router
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    ######### api path ##########################

    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

    #####user related path##########################
    path('', include('user.urls')),

    path('Login/', user_view.Login, name='Login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/login.html'), name='logout'),
    path('register/', user_view.register, name='register'),
    path('actionUrl/', user_view.actionUrl, name='actionUrl'),
    path('my_form/', user_view.my_form, name='my_form'),
    path('maindishes/', user_view.maindishes, name='maindishes'),
    path('RecipePagee/<int:pk>', user_view.RecipePagee, name='RecipePagee'),
    path('neww/', user_view.neww, name='neww'),
    path('Starters/', user_view.Starters, name='Starters'),
    path('Salads/', user_view.Salads, name='Salads'),
    path('Desserts/', user_view.Desserts, name='Desserts'),
    path('EmailSend/', user_view.EmailSend, name='EmailSend'),
    path('My_Recipe/', user_view.My_Recipe, name='My_Recipe'),
    path('my_form_edit/<int:pk>', user_view.my_form_edit, name='my_form_edit'),
    path('update/<int:pk>', user_view.update, name='update'),
    path('delete/<int:pk>', user_view.delete, name='delete'),
    path('NewIndex/', user_view.NewIndex, name='NewIndex'),
    path('NewIndex2/', user_view.NewIndex2, name='NewIndex2'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
