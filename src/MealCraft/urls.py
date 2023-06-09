"""
URL configuration for MealCraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from MealCraft.views import index,dev,loginpage,register_request, liste_request

urlpatterns = [
    path('', index, name="Accueil"),
    path('dev/', dev, name="Dev"),
    path('login/', loginpage, name="Login"),
    path("register/", register_request, name="register"),
    path("liste/", liste_request, name="liste"),



    path('admin/', admin.site.urls),
]


handler404 = "MealCraft.views.page_not_found_view"

