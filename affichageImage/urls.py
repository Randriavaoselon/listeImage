from django.urls import path
from affichageImage.views import affichage

urlpatterns = [
    path('', affichage, name="affiche"),
]