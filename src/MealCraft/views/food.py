from django.http import HttpResponse
from django.shortcuts import render

def noFood(request):
    return render(request, "404.html", {})

def foodGet(request, pk):
    return render(request, "food.html", {"code": str(pk)})
