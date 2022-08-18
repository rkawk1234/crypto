from django.http import HttpResponse
from django.shortcuts import render

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
