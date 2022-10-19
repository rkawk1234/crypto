from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('index.html',views.home, name ="home"),
    path('popularcryptos.html',views.popular, name="popular"),
    path('allcryptos.html',views.allcryp,name="allcryptos"),
    path('NFT.html',views.nft,name="nft"),
    path('aboutus.html',views.aboutus, name="aboutus"),
    path('signin.html',views.signin,name="signin"),
    path('register.html', views.register,name="register"),
    path('logout/', views.logoutUser, name="logout"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)