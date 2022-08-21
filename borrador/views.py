from django.http import HttpResponse
from django.shortcuts import render


def login(request):

    return render(request,"login.html")

def menu(request):

    return render(request,"menu.html")

def barra(request):

    return render(request,"barra.html")
