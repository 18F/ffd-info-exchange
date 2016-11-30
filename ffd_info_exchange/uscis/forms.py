from django import forms
from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USZipCodeField, USPhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
#from django_countries.fields import CountryField
#from django_countries.fields import LazyTypedChoiceField
#from django_countries.widgets import CountrySelectWidget

BLANK_CHOICE = (('', 'Choose one'))
# @maybe: Check how the N-400 handles nonbinary genders. The passport office
# doesn't issue documents with them but does accept documents with them.
GENDER_OPTIONS = (BLANK_CHOICE, ('female', 'Female'), ('male', 'Male'))
STATES = ((BLANK_CHOICE,) + STATE_CHOICES)
MARITAL_STATUS = (BLANK_CHOICE, ('single', 'Single'), ('married_or_remarried', 'Married or remarried'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('widowed', 'Widowed'))


class N400Step1(forms.Form):
    dummy_question = True


class N400Step2(forms.Form):
    # "Your current legal name (*do not* provide a nickname)""
    first_name = forms.CharField(label="Given name (First name)", required=False)
    middle_name = forms.CharField(label="Middle name (if applicable)", required=False)
    last_name = forms.CharField(label="Family name (Last name)", required=False)
    # Your name exactly as it appears on your permanent resident card (if applicable)
    # @todo: If we end up using both of these, find out which one should be carried through to the other form(s).
#    card_first_name = forms.CharField(label="Given name (First name)", required=False)
#    card_middle_name = forms.CharField(label="Middle name (if applicable)", required=False)
#    card_last_name = forms.CharField(label="Family name (Last name)", required=False)
    date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)', required=False)
    gender = forms.ChoiceField(choices=GENDER_OPTIONS, label="What is your gender?", required=False)
    country_of_birth = forms.CharField(label="Country of birth", required=False)
    ssn = USSocialSecurityNumberField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your application for naturalization.", required=False)
    email = forms.EmailField(label="Email address", required=False)
    # @todo: Tweak this to allow for non-U.S. phone numbers.
    phone = USPhoneNumberField(label="Telephone number", required=False)
    mailing_address_permanent = forms.CharField(label="Permanent mailing address (incl. apt. number)", required=False)
    mailing_address_city = forms.CharField(label="City", required=False)
    mailing_address_state = forms.ChoiceField(choices=STATES, label="State", required=False)
    # @maybe: Refactor as a USStateSelect.
    mailing_address_zip = USZipCodeField(label="ZIP code", required=False)
    # @maybe: Refactor these as CountryField()s.
    # Docs: https://pypi.python.org/pypi/django-countries#countryselectwidget
    country = forms.CharField(label="Country, if outside U.S.", required=False)
    country_of_citizenship = forms.CharField(label="Country of citizenship", required=False)
    other_names = forms.CharField(label="Other names you have used since birth", required=False)


class N400Step3(forms.Form):
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Current marital status", required=False)


class N400Step4(forms.Form):
    dummy_question = True


class N400Step5(forms.Form):
    dummy_question = True


class N400Step6(forms.Form):
    dummy_question = True
