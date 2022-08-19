from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

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

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request,'base/signin.html',context)