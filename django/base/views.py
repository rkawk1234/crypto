from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from .models import *
from .forms import CreateUserForm
# from .filters import OrderFilter


def home(request):
    return render(request,'base/index.html')

def popular(request):
    return render(request,'base/popularcryptos.html')

def allcryp(request):
    return render(request,'base/allcryptos.html')

def nft(request):
    return render(request,'base/NFT.html')

def aboutus(request):
    return render(request,'base/aboutus.html')

def signin(request):
    return render(request,'base/signin.html')

@csrf_exempt

def register(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}

    return render(request,'base/register.html',context)