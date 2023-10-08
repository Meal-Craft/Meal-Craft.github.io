from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from MealCraft.models import Liste

def noFood(request):
    """Si pas de demande URI renvoie une erreur 404"""
    return render(request, "404.html", {})


def foodGet(request, pk):
    """Renvoie la page de détails de produit
    
    Arguments:
        request {HttpRequest} -- requête HTTP
        pk {str} -- code nutrim du produit
    """
    
    ## Initialisation des variables
    inlist = None

    ## Vérification de l'authentification de l'utilisateur
    if request.user.is_authenticated:
        ## Vérification de l'existence du produit dans la liste de l'utilisateur
        inlist = Liste.objects.filter(user=request.user, nutrimcode=pk).exists()

        ## Si la requête est de type POST
        if request.method == "POST":

            ## Si le produit n'est pas dans la liste de l'utilisateur, on l'ajoute sinon ont le suppirme
            if not (Liste.objects.filter(user=request.user, nutrimcode=pk).exists()):
                Liste.objects.create(user=request.user, nutrimcode=pk)
            else:  
                Liste.objects.filter(user=request.user, nutrimcode=pk).delete()
            
            ## Redirection pour une actualisation de la page
            return redirect(f"/food/" + pk)

    return render(request, "food.html", {"code": str(pk), "inlist": inlist})
