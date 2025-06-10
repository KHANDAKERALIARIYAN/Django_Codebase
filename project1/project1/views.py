from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello you are at the Home page")
    return render(request, 'websites/home.html')

def about(request):
    # return HttpResponse("Hello you are at the About page")
    return render(request,'websites/about.html')

def contact(request):
    # return HttpResponse("Hello you are at the Contact page")
    return render(request,'websites/contact.html')
