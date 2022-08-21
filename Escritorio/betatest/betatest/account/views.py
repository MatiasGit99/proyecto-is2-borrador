from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required()
def tablero(request):
    return render(request,'account/tablero.html', {'section':'tablero'})

