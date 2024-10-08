"""
URL configuration for Guess_Game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

myapp = "guess_game"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , view=views.main_page , name="guess_game"),
    path("display_answer/" , view=views.display_answer , name="display_answer"),
    path("change_guess/" , view=views.change_guess , name="change_guess")

]
