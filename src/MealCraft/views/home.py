from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect

from MealCraft.models import Liste

import json

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Accueil"
        print(Liste.objects.filter(user=self.request.user))

        return context
    
    def post(self, request, **kwargs):     
        print("test")
        redirect(f"/liste")

        id = request.POST.get('id')
        print(id)

        return render(request, self.template_name, {})
