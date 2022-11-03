import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.base.decorators import unauthenticated_user
# Create your views here.
from .models import *
from .forms import CreateUserForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .decorators import unauthenticated_user
# from .filters import OrderFilter


popularapidata = requests.get('https://api.coingecko.com/api/v3/search/trending').json()
apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=250&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C7d').json()
apidata += requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=250&page=2&sparkline=true&price_change_percentage=1h%2C24h%2C7d').json()
apidata += requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=250&page=3&sparkline=true&price_change_percentage=1h%2C24h%2C7d').json()
apidata += requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=250&page=4&sparkline=true&price_change_percentage=1h%2C24h%2C7d').json()
nftapidata = requests.get('https://api.opensea.io/api/v1/collections?offset=0&limit=300').json()
rapidapidata = requests.get('https://cannaapi1.p.rapidapi.com/strains/orderbyrating').json()
# volumeList = []
# for i in apidata:
#     volumeList.append(i['total_volume'])
     
# volumeList.sort()


login_required(login_url='login')
def home(request):
    return render(request,'base/index.html', {'popularapidata':popularapidata, 'apidata':apidata})

def popular(request):

    
    return render(request,'base/popularcryptos.html',{'apidata':apidata})

def allcryp(request):
    
    return render(request,'base/allcryptos.html', {'apidata':apidata})


def nft(request):

    return render(request,'base/NFT.html',{'nftapidata':nftapidata})

def aboutus(request):
    return render(request,'base/aboutus.html', {'rapidapidata':rapidapidata})
    
@csrf_exempt
@unauthenticated_user
def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request,'base/signin.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@csrf_exempt
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('home')
    
    context = {'form': form}

    return render(request,'base/register.html',context)
