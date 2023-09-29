from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.shortcuts import render

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, label="Adresse email")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class RegisterView(TemplateView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "Enregistrement"
        context["result"] = ""

        if self.request.user.is_authenticated:
            return redirect(f"/")

        form = NewUserForm()

        context["register_form"] = form

        return context

    def post(self, request, **kwargs):
        form = NewUserForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            messages.success(self.request, "Registration successful." )
            return redirect(f"/")
        
        form = NewUserForm()
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return render(request, 'register.html', {'register_form': form})