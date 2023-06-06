from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
import openfoodfacts
from time import sleep
 

def index(request):
    if request.method == 'POST':
        logout(request)

    return render(request, "index.html", context={"page": "Accueil"})

def dev(request):
    if not request.user.is_authenticated:
        return redirect(f"/login/")
    
    barcode = "3017620422003"  # Remplacez par votre propre code-barres
    product = openfoodfacts.get_product(barcode)

    additives = openfoodfacts.facets.get_allergens()

    return render(request, 'dev.html', context={"page": "Dev", "product": product, "additives": additives})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def loginpage(request, **kwargs):
    result = ""

    if request.user.is_authenticated:
        return redirect(f"/")
    
    print(request)
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(f"/")
        else:
            result = "Mauvaise combinaison mot de passe - nom d'utilisateur"
    
    return render(request, "login.html", context={"page": "Login", "result": result})
    