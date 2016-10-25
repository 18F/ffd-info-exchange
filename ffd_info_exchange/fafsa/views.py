from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, FAFSA!")

def fafsa_form(request):
    return HttpResponse('<html><title>FAFSA</title></html')
