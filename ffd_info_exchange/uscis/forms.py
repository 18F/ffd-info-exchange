from django import forms
from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USZipCodeField, USPhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
#from django_countries.fields import CountryField
#from django_countries.fields import LazyTypedChoiceField
#from django_countries.widgets import CountrySelectWidget

BLANK_CHOICE = (('', 'Choose one'))
YES_OR_NO = (BLANK_CHOICE, ('1', 'Yes'), ('0', 'No'))
YES_OR_NO_RADIO = (('1', 'Yes'), ('0', 'No'))
YES_NO_MAYBE = (BLANK_CHOICE, ('1', 'Yes'), ('0', 'No'), ('2', 'Maybe'))
ELIGIBILITY_OPTIONS = (('0', "I’ve been a lawful permanent resident for at least five years."),
                       ('1', "I’ve been a lawful permanent resident for at least three years and I’ve been married to my spouse (a U.S. citizen) for at least three years. (As of the date I applied for citizenship, my spouse has been a U.S. citizen for at least three years.)"),
                       ('2', "I’ve been a lawful permanent resident for at least three years, I have a spouse who’s a U.S. citizen, and my spouse frequently participates in specified employment abroad."),
                       # @todo: Add help text for the above option:
                       # Help text: For more information on what qualifies as specified employment, check out these notes on the Immigration and Nationality Act, Section 319(b).
                       ('3', "I’m applying based on my qualifying military service. "),
                       ('4', "I’m applying for another reason."),
                       )
GENDER_OPTIONS = (BLANK_CHOICE, ('female', 'Female'), ('male', 'Male'))
EYE_COLOR_CHOICES = (('0', 'black'),
                     ('1', 'blue'),
                     ('2', 'brown'),
                     ('3', 'gray'),
                     ('4', 'green'),
                     ('5', 'hazel'),
                     ('6', 'maroon'),
                     ('7', 'pink'),
                     ('8', 'unknown/other')
                     )
HAIR_COLOR_CHOICES = (('0', 'bald (no hair)'),
                      ('1', 'black'),
                      ('2', 'blonde'),
                      ('3', 'brown'),
                      ('4', 'gray'),
                      ('5', 'red'),
                      ('6', 'sandy'),
                      ('7', 'white'),
                      ('8', 'unknown/other')
                      )

STATES = ((BLANK_CHOICE,) + STATE_CHOICES)
CONTACT_OPTIONS = (BLANK_CHOICE,
                   ('email', 'Email'),
                   ('phone', 'Primary phone number'),
                   ('phone_additional', 'Additional phone number'),
                   )
MARITAL_STATUS = (BLANK_CHOICE, ('single', 'Single'), ('married_or_remarried', 'Married or remarried'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('widowed', 'Widowed'))


class N400Step1(forms.Form):
    a_number = forms.IntegerField(label="Your nine-digit A-number", help_text="Your A-number is the eight- or nine-digit number on your Permanent Resident Card.", required=False)
    not_a_minor = forms.ChoiceField(label="Are you at least 18 years old?", choices=YES_OR_NO, widget=forms.RadioSelect, required=False)
    why_eligible = forms.ChoiceField(label="How are you eligible to apply for citizenship?", choices=ELIGIBILITY_OPTIONS, widget=forms.RadioSelect, required=False)
    # @todo: Reinstate that radio button issue.


class N400Step2(forms.Form):
    # "Your current legal name"
    last_name = forms.CharField(label="Last name (family name)", required=False)
    first_name = forms.CharField(label="First name (given name)", required=False)
    middle_name = forms.CharField(label="Middle name (if applicable)", required=False)
    other_names = forms.CharField(label="Have you ever used any other names? If so, please list them", help_text="Include nicknames, aliases, and your maiden name, if applicable.", required=False)
    # @todo: Determine whether to add "Would you like to legally change your name?" here or elsewhere.
    ssn = USSocialSecurityNumberField(label="U.S. Social Security number (if you have one)", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your application for naturalization.", required=False)
    # @todo: Determine whether that help text ^ is still accurate.
    uscis_acct_number = forms.CharField(label="USCIS online account number (if you have one)", required=False)
    # ^ If this were a live app, we'd add validation and more specifics. It
    # isn't, so we won't spend time on that now.
    gender = forms.ChoiceField(choices=GENDER_OPTIONS, label="What is your gender?", required=False)
    height_pt1 = forms.IntegerField(label="Height, feet", required=False)
    height_pt2 = forms.IntegerField(label="Height, inches", required=False)
    # @todo: Adjust the display of the above so they're reasonable.
    weight = forms.IntegerField(label="Weight in pounds", required=False)
    # @todo: Fix rendering of these checkboxes.
    eye_color = forms.ChoiceField(label="Eye color", choices=EYE_COLOR_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    hair_color = forms.ChoiceField(label="Hair color", choices=HAIR_COLOR_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)', required=False)
    date_of_residency = forms.DateTimeField(label='Date you became a Lawful Permanent Resident (MM/DD/YYYY)', required=False)
    country_of_birth = forms.CharField(label="Country of birth", required=False)
    city_of_birth = forms.CharField(label="City of birth", required=False)
    country_of_citizenship = forms.CharField(label="Country of citizenship or nationality", required=False)
    # "Current residential address"
    residential_address_street = forms.CharField(label="Street number and name", required=False)
    residential_address_apt = forms.CharField(label="Apartment or floor number (if applicable)", required=False)
    residential_address_city = forms.CharField(label="City", required=False)
    residential_address_state = forms.ChoiceField(choices=STATES, label="State", required=False)
    # @maybe: Refactor as a USStateSelect.
    residential_address_zip = USZipCodeField(label="ZIP code", required=False)
    # @maybe: Refactor these as CountryField()s.
    # Docs: https://pypi.python.org/pypi/django-countries#countryselectwidget
    residential_address_country = forms.CharField(label="Country, if outside the U.S.", required=False)
    dates_of_residence = forms.CharField(label="Dates of residence (ex: from MM/DD/YYYY to present", required=False)
    # Is your mailing address different than your residential address?
    # or: If you have a different mailing address:
    mailing_address_street = forms.CharField(label="Mailing address street number and name", required=False)
    mailing_address_apt = forms.CharField(label="Apartment or floor number (if applicable)", required=False)
    mailing_address_city = forms.CharField(label="City", required=False)
    mailing_address_state = forms.ChoiceField(choices=STATES, label="State", required=False)
    # @maybe: Refactor as a USStateSelect.
    mailing_address_zip = USZipCodeField(label="ZIP code", required=False)

    email = forms.EmailField(label="Email address", required=False)
    # @todo: Tweak this to allow for non-U.S. phone numbers. Add country code field.
    phone_primary = USPhoneNumberField(label="Primary phone number", required=False)
    phone_additional = USPhoneNumberField(label="Additional phone number", required=False)

    how_to_contact = forms.ChoiceField(label='How would you like us to contact you?', choices=CONTACT_OPTIONS, required=False)
    occupation = forms.CharField(label="Occupation", required=False)
    employer_name = forms.CharField(label="Name of your current employer or school", required=False)


class N400Step3(forms.Form):
    # @todo: Fill in the remaining questions.
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Current marital status", required=False)


class N400Step4(forms.Form):
    # Moral character
    taxes_owe = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Do you owe any overdue local, state, or federal taxes?', required=False)
    taxes_not_filed = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Have you ever not filed any local, state, or federal taxes?', required=False)
    felony_convicted = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Have you ever been convicted of or pled guilty to a felony?', required=False)
    felony_insanity = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Have you ever been found not guilty of a felony by reason of insanity?', required=False)
    felony_recent = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Within the past seven years, have you been convicted of a felony?', required=False)
    incarceration_recent = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Within the past five years, have you been released from incarceration?', required=False)
    # "Were you ever, in any way, involved with any of the following?"
    genocide = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Genocide?', required=False)
    torture = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Torture?', required=False)
    murder = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Killing, or trying to kill, someone?', required=False)
    harm = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Badly hurting, or trying to hurt, a person on purpose?', required=False)
    sexual_assault = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Forcing, or trying to force, someone to have any kind of sexual contact or relations?', required=False)
    repressing_religion = forms.ChoiceField(choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, label='Not letting someone practice their religion?', required=False)


class N400Step5(forms.Form):
    # Evidence for your application
    add_custom_template = True


class N400Step6(forms.Form):
    # Review your application
    add_custom_template = True
    # In the forthcoming template, include a representation of the data thus far.


class N400Step7(forms.Form):
    # Sign and pay
    signature_applicant = forms.CharField(label="Applicant's signature", required=True)
    signature_translator = forms.CharField(label="Translator's signature (if applicable)", required=False)


class AdditionalServices(forms.Form):
    # If we take a click-individual-buttons-and-return approach, we don't need
    # to store this information. If we take the click-checkboxes-and-queue-them
    # -up approach, it may be appropriate to have actual fields here.
    placeholder = True


class NameChange(forms.Form):
    desired_first_name = forms.CharField(label="First name (given name)", required=False)
    desired_middle_name = forms.CharField(label="Middle name (if applicable)", required=False)
    desired_last_name = forms.CharField(label="Last name (family name)", required=False)


class TSAPreCheck(forms.Form):
    phone_country_code = forms.IntegerField(label="Phone country code", required=False)
    names_match = forms.ChoiceField(label="Do the names on the identity documents you've already provided match the name on your birth certificate?", choices=YES_OR_NO_RADIO, widget=forms.RadioSelect, help_text="If the names on your identity documents don’t match the name you were given at birth, you’ll need to provide additional documentation.", required=False)
    how_many_documents = forms.IntegerField(label="How many documents are you providing to show that the name you’re enrolling under is the same as your current name?", required=False)
    under_indictment_tsa = forms.ChoiceField(label="Are you under indictment for qualifying crimes outlined by the TSA?", choices=YES_OR_NO_RADIO, help_text="For a list of qualifying crimes, see https://www.tsa.gov/Disqualifying-Offenses-Factors", widget=forms.RadioSelect, required=False)


class Passport(forms.Form):
    dummy_question = True
