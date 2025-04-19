from django.shortcuts import render

def home(request):
    return render(request, 'presentation/home.html')