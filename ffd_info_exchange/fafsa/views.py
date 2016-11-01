from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
#from .models import Application


def fafsa_form(request):
#    form = FAFSAApplicationForm(request.POST or None)
    form = FAFSAApplicationForm1
#    if form.is_valid():
#        application = form.save()
#        return redirect(confirmation_screen)
    return render(request, 'fafsa_form.html', {'form': form})
