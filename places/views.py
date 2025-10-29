from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def place1(request):
    return render(request, 'place1.html')

def place2(request):
    return render(request, 'place2.html')

def place3(request):
    return render(request, 'place3.html')

def place4(request):
    return render(request, 'place4.html')

def place5(request):
    return render(request, 'place5.html')
