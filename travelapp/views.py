from django.shortcuts import render
from .models import host, own


# Create your views here.
def drive(request):
    fet = host.objects.all
    bet = own.objects.all
    return render(request, "index.html", {'re': fet, 'le': bet})
