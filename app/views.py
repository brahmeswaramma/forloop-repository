from django.shortcuts import render

# Create your views here.

def Einstein(request):
    return render(request,'Einstein.html')

def newton(request):
    return render(request,'newton.html')

def darwin(request):
    return render(request,'darwin.html')

