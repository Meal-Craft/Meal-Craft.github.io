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

from MealCraft.views import HomeView, ListeView, LoginView, LogoutView, RegisterView, noFood, foodGet

urlpatterns = [
    path('', HomeView.as_view(), name="Accueil"),
    path('login/', LoginView.as_view(), name="Login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("liste/", ListeView.as_view(), name="liste"),
    path('logout/', LogoutView.as_view(), name="Logout"),

    path("food/", noFood, name="Nouriture"),
    path("food/<str:pk>/", foodGet, name="Nouriture"),

    path('klopdfsjopigjpoerjrgopergopgperogeropopkerg/', admin.site.urls),
]


#handler404 = "MealCraft.views.ErrorView"

