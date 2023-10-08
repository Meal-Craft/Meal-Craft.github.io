from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

class LoginView(TemplateView):
    """Vue de la page de connexion"""
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        ## Initialisation des variables
        context = super().get_context_data(**kwargs)
        context["Page"] = "Connexion"
        context["result"] = ""

        ## Si l'utilisateur est authentifié, on le redirige vers la page d'accueil
        if self.request.user.is_authenticated:
            return redirect(f"/")

        return context


    def post(self, request, **kwargs):     
        """Fonction de récupération du formulaire de connexion"""

        ## Récupération des données du formulaire
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        ## Authentification de l'utilisateur
        user = authenticate(username=username, password=password)

        ## Si le compte est valide, on connecte l'utilisateur sinon ont renvoie une erreur
        if user is not None and user.is_active:
            login(request, user)
            return redirect(f"/")
        else:
            result ="Mauvaise combinaison mot de passe - nom d'utilisateur"
        
        return render(request, 'login.html', {'result': result})
    