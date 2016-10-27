from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USStateField
#from django import forms
#from .models import Application
#@todo: Reinstate when actually wiring this up.
import floppyforms.__future__ as forms


class FAFSAApplicationForm(forms.Form):
    first_name = forms.CharField(label="Your first name")
    last_name = forms.CharField(label="Your last name")
    date_of_birth = forms.DateTimeField(label='Your date of birth (MM/DD/YYYY)')
