from django.shortcuts import render
from .models import portfolio

# Create your views here.
def home(request):
    port=portfolio.objects.all()
    return render(request,'portfolio/home.html',{'port':port})
