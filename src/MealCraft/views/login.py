from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

class LoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Connexion"
        context["result"] = ""

        if self.request.user.is_authenticated:
            return redirect(f"/")

        return context


    def post(self, request, **kwargs):     
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(f"/")
        else:
            result ="Mauvaise combinaison mot de passe - nom d'utilisateur"
        
        return render(request, 'login.html', {'result': result})
    