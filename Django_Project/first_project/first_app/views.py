from django.shortcuts import render, HttpResponse

def myPortfolio(request):
    return render(request,'home.html')

