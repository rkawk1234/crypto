from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('index.html',views.home),
    path('popularcryptos.html',views.popular),
    path('allcryptos.html',views.allcryp),
    path('NFT.html',views.nft),
    path('aboutus.html',views.aboutus),
    path('signin.html',views.signin),
    path('register.html', views.register),
    path('logout/', views.logoutUser, name="logout"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)