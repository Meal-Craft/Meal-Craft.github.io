from django.views.generic import TemplateView
from django.shortcuts import redirect

from MealCraft.models import Liste

import json

class ListeView(TemplateView):
    """Vue de la page de la liste de produit"""
    template_name = "liste.html"

    def get_context_data(self, **kwargs):
        ## Initialisation des variables
        context = super().get_context_data(**kwargs)
        context["Page"] = "Liste"
        context["liste"] = Liste.objects.filter(user=self.request.user)

        ## Si l'utilisateur n'est pas authentifié, on le redirige vers la page de connexion
        if not self.request.user.is_authenticated:
            return redirect(f"/login/")
    
        return context
