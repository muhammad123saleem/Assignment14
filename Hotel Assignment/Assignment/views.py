#from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #return HttpResponse("Hello world I am home page")
    return render(request, 'home.html')
def about_page(request):
    #return HttpResponse("Hello world I am home page")
    return render(request, 'about.html')