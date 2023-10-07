from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from MealCraft.models import Liste

def noFood(request):
    return render(request, "404.html", {})

def foodGet(request, pk):
    inlist = None
    if request.user.is_authenticated:
        inlist = Liste.objects.filter(user=request.user, nutrimcode=pk).exists()

        if request.method == "POST":
            if not (Liste.objects.filter(user=request.user, nutrimcode=pk).exists()):
                Liste.objects.create(user=request.user, nutrimcode=pk)

                return redirect(f"/food/" + pk)

    return render(request, "food.html", {"code": str(pk), "inlist": inlist})
