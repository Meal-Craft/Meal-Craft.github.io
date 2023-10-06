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
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Accueil"
        print("test")

        context["liste"] = {}
        print(context["liste"])
        
        if self.request.user.is_authenticated:
            context["liste"] = serialize('json', Liste.objects.filter(user=self.request.user))
            print(context["liste"])

        return context
    
    def post(self, request, **kwargs):     
        if request.user.is_authenticated:
            print("test")
            redirect(f"/liste")

            id = request.POST.get('id')
            print(id)

        return render(request, self.template_name, {})
