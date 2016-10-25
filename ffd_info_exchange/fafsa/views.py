from django.shortcuts import render
from django.http import HttpResponse


def fafsa_form(request):
    return render(request, '<html><title>FAFSA</title></html>')
