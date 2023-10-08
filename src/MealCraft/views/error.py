from django.views.generic import TemplateView

class ErrorView(TemplateView):
    """Vue de la page d'erreur 404"""
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        ## Initialisation des variables
        context = super().get_context_data(**kwargs)
        context["Page"] = "404 Error"

        return context
