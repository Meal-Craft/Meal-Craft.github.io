from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout


class LogoutView(TemplateView):
    """Vue de déconnexion"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ## déconnexion de l'utilisateur
        logout(self.request)

        return context
    
