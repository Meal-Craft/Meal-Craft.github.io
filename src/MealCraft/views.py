from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.contrib import messages
 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import requests, json

def get_unique_foods(search_query):
    api_url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={search_query}&search_simple=1&action=process&json=1'

    response = requests.get(api_url)
    data = response.json()

    if 'products' in data:
        products = data['products']
        unique_foods = []
        for product in products:
            if 'product_name' in product:
                unique_foods.append(product['product_name'])
        return list(set(unique_foods))
    else:
        return []

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, label="Adresse email")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

def index(request):
    if request.method == 'POST':
        logout(request)

    return render(request, "index.html", context={"page": "Accueil"})

def dev(request):
    if not request.user.is_authenticated:
        return redirect(f"/login/")
      
    unique_foods = get_unique_foods("eau")
    print(unique_foods)
    
    return render(request, 'dev.html', context={"page": "Dev", "product": product})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def loginpage(request, **kwargs):
    result = ""

    if request.user.is_authenticated:
        return redirect(f"/")
    
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
    
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(f"/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html", context={"register_form":form})

def liste_request(request):
    if request.method == 'POST':
        logout(request)
    return render(request, "liste.html", context={"page": "Liste"})
