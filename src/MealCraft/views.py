from django.shortcuts import render

def index(request):
    return render(request, "index.html", context={"page": "Accueil"})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)