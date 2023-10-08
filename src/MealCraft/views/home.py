from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.serializers import serialize

from MealCraft.models import Liste

import json

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    """Vue de la page d'accueil"""
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ## Initialisation des variables
        context["Page"] = "Accueil"
        context["liste"] = {}
        
        ## Si l'utilisateur est authentifié, on récupère sa liste de produit
        if self.request.user.is_authenticated:
            context["liste"] = serialize('json', Liste.objects.filter(user=self.request.user))

        return context
    
    # def post(self, request, **kwargs):     
    #     if request.user.is_authenticated:
    #         print("test")
    #         redirect(f"/liste")

    #         id = request.POST.get('id')
    #         print(id)

    #     return render(request, self.template_name, {})
