from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from formtools.wizard.views import SessionWizardView


class FAFSAWizard(SessionWizardView):
    template_name = "fafsa_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)

        return render_to_response('confirmation.html', {'form_data': form_data})

    def process_form_data(form_list):
        form_data = [form.cleaned_data for form in form_list]

        return form_data
