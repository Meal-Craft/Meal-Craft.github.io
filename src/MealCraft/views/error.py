from django.views.generic import TemplateView

class ErrorView(TemplateView):
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Page"] = "404 Error"
        return context
