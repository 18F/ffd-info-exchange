from django.shortcuts import render
from django.http import HttpResponse


def fafsa_form(request):
    return render(request, 'fafsa_form.html')
