from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USStateField
#from django import forms
#from .models import Application
#@todo: Reinstate when actually wiring this up.
import floppyforms.__future__ as forms


class FAFSAApplicationForm(forms.Form):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    ssn = localflavor.USSocialSecurityNumberField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your FAFSA.")
    date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)')
