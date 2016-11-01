from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USStateSelect, USZipCodeField, USPSSelect, USPhoneNumberField
from django import forms
#from .models import Application
#import floppyforms.__future__ as forms

YES_OR_NO = (('1', 'Yes'), ('0', 'No'))
YES_NO_MAYBE = (('1', 'Yes'), ('0', 'No'), ('2', 'Maybe'))
GENDER_OPTIONS = (('female', 'Female'), ('male', 'Male'))
MARITAL_STATUS = (('single', 'Single'), ('married_or_remarried', 'Married or remarried'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('widowed', 'Widowed'))
CITIZENSHIP_STATUS = (('yes', "Yes, I'm a U.S. citizen (or U.S. national)"), ('no_but_eligible', "No, but I'm an eligible noncitizen"), ('not_at_all', "No, I'm not a citizen or eligible noncitizen"))
SCHOOL_COMPLETION_STATUS = (('diploma', "I’ll have a high school diploma"), ('ged', "I’ll have a GED certificate or state-authorized high school equivalent certificate"), ('home_schooled', "I was home schooled and will have completed my curriculum"), ('none', "None of the above"))
COLLEGE_GRADE_LEVEL = (('0', "First-year student (never attended college)"), ('1', "First-year student (attended college before)"), ('2', "Second-year student (sophomore)"), ('3', "Third-year student (junior)"), ('4', "Fourth-year student (senior)"), ('5', "Fifth-year student (other undergraduate)"), ('6', "First-year graduate/professional student"), ('grad_continuing', "Continuing graduate/professional student/beyond"))
DEGREES = (('1', "First bachelor’s degree"), ('2', "Second bachelor’s degree"), ('3', "Associate degree (occupational or technical program)"), ('4', "Associate degree (general education/transfer program)"), ('5', "Certificate/diploma (occupational/technical/educational program of less than two years)"), ('6', "Certificate/diplomat (occupational/technical/educational program of at least two years)"), ('7', "Teaching credential program (nondegree)"), ('8', "Graduate or professional degree"), ('9', "Other or undecided"))
PARENTS_SCHOOL_COMPLETION = (('middle'), ("Middle school/junior high")), (('high'), ("High school")), (('college'), ("College or beyond")), (('not_sure'), ("I don’t know")),


class FAFSAApplicationForm(forms.Form):
    # "Your demographic information" section
    # To start the application process, we'll need to collect some basic information about you.
    first_name = forms.CharField(label="First name")
    middle_initial = forms.CharField(label="Middle initial", max_length=1)
    last_name = forms.CharField(label="Last name")
    ssn = localflavor.USSocialSecurityNumberField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your FAFSA.")
    date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)')
    assigned_sex = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_OPTIONS, label="What gender do you identify with?")
    mailing_address_permanent = forms.CharField(label="Permanent mailing address (incl. apt number")
    mailing_address_city = forms.CharField(label="City")
    mailing_address_country = forms.CharField(label="Country, if not U.S.", required=False)  # @todo: Incorporate localflavor
    mailing_address_state = localflavor.USStateSelect()  # @todo: Fix this.
    mailing_address_zip = localflavor.USZipCodeField(label="ZIP code")
    state_five_years = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_OR_NO, label="Have you lived in your state for at least five years?")
    usps = localflavor.USPSSelect()  # @todo: Determine whether this is relevant.
    phone = localflavor.USPhoneNumberField(label="Telephone number")
    email = forms.EmailField(label="Email address")
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Current marital status")
    drivers_license = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_OR_NO, label="Do you have driver's license information that you'd like to share?")
    # @todo: Add conditional driver's license number.
    # @todo: Add conditional driver's license state (dropdown select).

    # "Your financial aid eligibility" section
    # Please answer these questions to help us determine whether you’re eligible for financial aid.
    us_citizen = forms.ChoiceField(choices=CITIZENSHIP_STATUS, label="Are you a U.S. citizen?")
    high_school_status = forms.ChoiceField(choices=SCHOOL_COMPLETION_STATUS, label="What will your high school completion status be when you begin college in the 2017-2018 school year?")
    entering_grade_level = forms.ChoiceField(choices=COLLEGE_GRADE_LEVEL, label="What will your college grade level be when you begin the 2017-2018 school year?")
    degree_pursued = forms.ChoiceField(choices=DEGREES, label="What degree or certificate will you be working on when you begin the 2017-2018 school year?")
    work_study = forms.ChoiceField(choices=YES_NO_MAYBE, label="Would you like to be considered for work study?")
    has_degree = forms.ChoiceField(choices=YES_OR_NO, label="Will you have your first bachelor's degree before you begin the 2017-2018 school year?")
    foster_youth = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_OR_NO, label="Are you a foster youth, or were you ever in the foster care system?")
    completed_parent_1 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 1")
    completed_parent_2 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 2")

    # "Your financial aid eligibility, continued" section
    high_school_name = forms.CharField(label="What is the name of your high school?")
    high_school_city = forms.CharField(label="In what city is your high school?")
    # @todo: Fix this next one. label="In what state is your high school?"
    high_school_state = localflavor.USStateSelect()
