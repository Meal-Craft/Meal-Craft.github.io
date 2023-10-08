from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.shortcuts import render

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, label="Adresse email")

	class Meta:
        ## On recupère la table utilisateur
		model = User
        ## On définit les champs du formulaire
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
        ## On enregistre l'utilisateur
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class RegisterView(TemplateView):
    """Vue de la page d'enregistrement"""
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        ## Initialisation des variables
        context = super().get_context_data(**kwargs)
        context["Page"] = "Enregistrement"
        context["result"] = ""

        ## Si l'utilisateur est authentifié, on le redirige vers la page d'accueil
        if self.request.user.is_authenticated:
            return redirect(f"/")

        ## Création du formulaire d'enregistrement
        form = NewUserForm()

        ## renvoie le formulaire
        context["register_form"] = form

        return context

    def post(self, request, **kwargs):
        """Fonction de récupération du formulaire d'enregistrement"""
        form = NewUserForm(self.request.POST)
        
        ## Si le formulaire est valide, on enregistre l'utilisateur et on le connecte
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return redirect(f"/")
        
        ## Sinon on renvoie une erreur et un nouveau formulaire
        form = NewUserForm()
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return render(request, 'register.html', {'register_form': form})