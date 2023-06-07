from django.shortcuts import render
import openfoodfacts

def index(request):
    return render(request, "index.html", context={"page": "Accueil"})

def dev(request):
    barcode = "3017620422003"  # Remplacez par votre propre code-barres
    product = openfoodfacts.get_product(barcode)

    additives = openfoodfacts.facets.get_allergens()
    print(additives)
    


    return render(request, 'dev.html', context={"page": "Dev", "product": product, "additives": additives})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)