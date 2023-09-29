from django.views.generic import TemplateView
from django.shortcuts import redirect

from MealCraft.models import Liste

class ListeView(TemplateView):
    template_name = "liste.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Liste"
        context["liste"] = Liste.objects.filter(user=request.user)

        if not self.request.user.is_authenticated:
            return redirect(f"/login/")
    
        return context
