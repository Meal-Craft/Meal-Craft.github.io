from django.views.generic import TemplateView
from django.shortcuts import redirect

from MealCraft.models import Liste


class DevView(TemplateView):
    template_name = "dev.html"

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Dev"

        if not request.user.is_authenticated:
            return redirect(f"/login/")
        
        Liste.objects.create(user=request.user, nutrimcode="3274080005003")
        Liste.objects.create(user=request.user, nutrimcode="3017620422003")
        Liste.objects.create(user=request.user, nutrimcode="7622210449283")
        Liste.objects.create(user=request.user, nutrimcode="5449000214911")

        return context
