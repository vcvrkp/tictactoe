"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, new_invitation, accept_invitation

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('welcome/', welcome),
    url(r'home$', home, name="player_home"),
    url(r'login$',LoginView.as_view(template_name="player/login_form.html"),name="player_login"),
    # url(r'^$', welcome),
    url(r'logout$',LogoutView.as_view(),name="player_logout"),
    url(r'new_invitation$',new_invitation,name="player_new_invitation"),
    url(r'accept_invitation/(?P<id>\d+)/$',accept_invitation,name="player_accept_invitation")
]
