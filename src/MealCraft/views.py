from django.shortcuts import render
import requests
import openfoodfacts

def index(request):
    return render(request, "index.html", context={"page": "Accueil"})

def dev(request):
    barcode = "3017620422003"  # Remplacez par votre propre code-barres
    product = openfoodfacts.get_product(barcode)

    if product:
        print("Nom : ", product["product"]["product_name"])
        print("Code : ", product["code"])
        print("Nutriscore : ", product["product"]["nutriscore_data"]["grade"])


    else:
        print("Produit non trouvé.")

    return render(request, 'dev.html', context={"page": "Dev"})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)