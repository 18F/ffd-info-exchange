from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USStateSelect, USZipCodeField, USPSSelect, USPhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
from django import forms
#import floppyforms.__future__ as floppyforms

BLANK_CHOICE = (('', 'Choose one'))
YES_OR_NO = (BLANK_CHOICE, ('1', 'Yes'), ('0', 'No'))
YES_NO_MAYBE = (BLANK_CHOICE, ('1', 'Yes'), ('0', 'No'), ('2', 'Maybe'))
GENDER_OPTIONS = (BLANK_CHOICE, ('female', 'Female'), ('male', 'Male'))
MARITAL_STATUS = (BLANK_CHOICE, ('single', 'Single'), ('married_or_remarried', 'Married or remarried'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('widowed', 'Widowed'))
STATES = ((BLANK_CHOICE,) + STATE_CHOICES)
CITIZENSHIP_STATUS = (BLANK_CHOICE, ('yes', "Yes, I'm a U.S. citizen (or U.S. national)"), ('no_but_eligible', "No, but I'm an eligible noncitizen"), ('not_at_all', "No, I'm not a citizen or eligible noncitizen"))
SCHOOL_COMPLETION_STATUS = (BLANK_CHOICE, ('diploma', "I’ll have a high school diploma"), ('ged', "I’ll have a GED certificate or state-authorized high school equivalent certificate"), ('home_schooled', "I was home schooled and will have completed my curriculum"), ('none', "None of the above"))
COLLEGE_GRADE_LEVEL = (BLANK_CHOICE, ('0', "First-year student (never attended college)"), ('1', "First-year student (attended college before)"), ('2', "Second-year student (sophomore)"), ('3', "Third-year student (junior)"), ('4', "Fourth-year student (senior)"), ('5', "Fifth-year student (other undergraduate)"), ('6', "First-year graduate/professional student"), ('grad_continuing', "Continuing graduate/professional student/beyond"))
DEGREES = (BLANK_CHOICE, ('1', "First bachelor’s degree"), ('2', "Second bachelor’s degree"), ('3', "Associate degree (occupational or technical program)"), ('4', "Associate degree (general education/transfer program)"), ('5', "Certificate/diploma (occupational/technical/educational program of less than two years)"), ('6', "Certificate/diplomat (occupational/technical/educational program of at least two years)"), ('7', "Teaching credential program (nondegree)"), ('8', "Graduate or professional degree"), ('9', "Other or undecided"))
PARENTS_SCHOOL_COMPLETION = (BLANK_CHOICE, ('middle', "Middle school/junior high"), ('high', "High school"), ('college', "College or beyond"), ('not_sure', "I don’t know"))
TAX_COMPLETION_STATUS_STUDENT = (BLANK_CHOICE, ('already_filed', "I already completed my tax return"), ('will_file', "I will file my tax return"), ('wont_file', "I'm not going to file my tax return"))
TAX_FILING_STATUS = (BLANK_CHOICE, ('single', "Single"), ('head', "Head of household"), ('joint', "Married — filed joint return"), ('separate', "Married — filed separate returns"), ('widowed', "Qualifying widow or widower"), ('not_sure', "I’m not sure"))
TAX_FORM_TYPES = (BLANK_CHOICE, ('1040', "IRS 1040"), ('1040a', "IRS 1040A or 1040EZ"), ('foreign', "Foreign tax return"), ('associated', "A tax return with Puerto Rico, a U.S. territory, or a freely associated state"))
CONSENT_TO_RETRIEVE_DATA = (BLANK_CHOICE, ('1', 'I allow the IRS to import my 2015 tax information.'), ('0', 'Do not import my 2015 tax information — I’ll enter it manually.'))
BENEFIT_PROGRAMS = (('medicaid', "Medicaid"), ('ssi', "Supplemental Security Income (SSI)"), ('snap', "Supplemental Nutrition Assistance Program (SNAP)"), ('lunch', "Free or reduced-price school lunch"), ('tanf', "Temporary Assistance for Needy Families (TANF)"), ('wic', "Special Supplemental Nutrition Program for Women, Infants, and Children (WIC)"), ('none', "None of the above"))
FORM_FILLER = (BLANK_CHOICE, ('student', "Student"), ('preparer', "Preparer"))


class FAFSAApplicationForm1(forms.Form):
    # "Your demographic information" section
    # To start the application process, we'll need to collect some basic information about you.
    first_name = forms.CharField(label="First name", required=False)
    middle_initial = forms.CharField(label="Middle initial (if applicable)", max_length=1, required=False)
    last_name = forms.CharField(label="Last name", required=False)
    #ssn = localflavor.USSocialSecurityNumberField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your FAFSA.", required=False)
    ssn = forms.CharField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your FAFSA.", required=False)
    #date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)', required=False)
    date_of_birth = forms.CharField(label='Date of birth (MM/DD/YYYY)', required=False)
    assigned_sex = forms.ChoiceField(choices=GENDER_OPTIONS, label="What gender were you designated at birth?", required=False)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Current marital status", required=False)


class FAFSAApplicationForm2(forms.Form):
    mailing_address_permanent = forms.CharField(label="Permanent mailing address (incl. apt. number)", required=False)
    mailing_address_city = forms.CharField(label="City", required=False)
    mailing_address_state = forms.ChoiceField(choices=STATES, label="State", required=False)
    #mailing_address_zip = localflavor.USZipCodeField(label="ZIP code", required=False)
    #phone = localflavor.USPhoneNumberField(label="Telephone number", required=False)
    #email = forms.EmailField(label="Email address", required=False)
    mailing_address_zip = localflavor.CharField(label="ZIP code", required=False)
    phone = localflavor.CharField(label="Telephone number", required=False)
    email = forms.CharField(label="Email address", required=False)


class FAFSAApplicationForm3(forms.Form):
    # "Your financial aid eligibility" section
    # Please answer these questions to help us determine whether you’re eligible for financial aid.
    us_citizen = forms.ChoiceField(choices=CITIZENSHIP_STATUS, label="Are you a U.S. citizen?", required=False)
    high_school_status = forms.ChoiceField(choices=SCHOOL_COMPLETION_STATUS, label="What will your high school completion status be when you begin college in the 2017-2018 school year?", required=False)
    entering_grade_level = forms.ChoiceField(choices=COLLEGE_GRADE_LEVEL, label="What will your college grade level be when you begin the 2017-2018 school year?", required=False)
    degree_pursued = forms.ChoiceField(choices=DEGREES, label="What degree or certificate will you be working on when you begin the 2017-2018 school year?", required=False)
    work_study = forms.ChoiceField(choices=YES_NO_MAYBE, label="Would you like to be considered for work study?", required=False)
    has_degree = forms.ChoiceField(choices=YES_OR_NO, label="Will you have your first bachelor's degree before you begin the 2017-2018 school year?", required=False)
    foster_youth = forms.ChoiceField(choices=YES_OR_NO, label="Are you a foster youth, or were you ever in the foster care system?", required=False)
    completed_parent_1 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 1", required=False)
    completed_parent_2 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 2", required=False)


class FAFSAApplicationForm4(forms.Form):
    # "Dependency determination" section
    has_dependents_children = forms.ChoiceField(choices=YES_OR_NO, label="Do you now have or will you have children who will receive more than half of their support from you between July 1, 2017 and June 30, 2018?", required=False)
    has_dependents_non_children = forms.ChoiceField(choices=YES_OR_NO, label="Do you have dependents (other than your children or spouse) who live with you and who receive more than half of their support from you, now and through June 30, 2018?", required=False)
    household_size = forms.IntegerField(label="Your number of household members in 2017-2018", min_value=1, required=False)
    num_household_college = forms.IntegerField(label="How many people in your household will be in college in 2017-2018?", min_value=0, required=False)


class FAFSAApplicationForm5(forms.Form):
    # "Student tax information" section
    # Thanks for sharing your parents’ financial information. Now we have a
    # few questions about your tax information.
    # ^ @todo: Consider making this phrasing more accommodating of 'parent'.
    student_taxes_completed = forms.ChoiceField(choices=TAX_COMPLETION_STATUS_STUDENT, label="For 2015, have you completed your IRS income tax return or another tax return?", required=False)
    consent_to_retrieve_data = forms.ChoiceField(choices=CONSENT_TO_RETRIEVE_DATA, label="Use the Data Retrieval Tool to import your tax data.", help_text="Why import your data? Allowing the IRS to share your tax information saves time and is more accurate than manually completing this section. The IRS uses your full legal name and Social Security number to retrieve your tax information. \n\nThe Department of Education will not store any of your tax information after your FAFSA is processed.", required=False)


class FAFSAApplicationForm6(forms.Form):
    student_agi = forms.IntegerField(label="What was your adjusted gross income for 2015?", min_value=0, help_text="You can find this number on IRS Form 1040, line 37.", required=False)
    student_earned = forms.IntegerField(label="How much did you earn from working (including wages, salaries, and tips) in 2015?", min_value=0, help_text="Calculate this by adding lines 7, 12, and 18 of the IRS Form 1040.", required=False)
    student_is_dislocated = forms.ChoiceField(choices=YES_NO_MAYBE, label="As of today, are you a dislocated worker?", required=False)
    # student_received_benefits = forms.MultipleChoiceField(choices=BENEFIT_PROGRAMS, label="In 2015 or 2016, did you or anyone in your household receive benefits from any of the federal programs listed below? Select all that apply or select 'None of the above' if you didn't receive any benefits. If, at the time you are completing the FAFSA, you or anyone in your household did NOT receive any of these benefits during 2015 or 2016, but will receive any of them on or before December 31, 2016, you must return to the FAFSA and update your response.", help_text="Please note that answering these questions won’t impact your eligibility for these programs or student aid.", required=False)
    # @todo: Check that the corresponding parent text is in line with this. ^ There may have been half a dropped sentence.
    student_eligible_for_simpler = forms.ChoiceField(choices=YES_NO_MAYBE, label="You let us know that you completed a 2015 IRS Form 1040. Were you eligible to file an IRS 1040A or 1040EZ?", required=False)


class FAFSAApplicationForm7(forms.Form):
    student_tax_paid = forms.IntegerField(label="How much income tax did you pay in 2015?", min_value=0, help_text="Calculate this by subtracting line 46 from line 56 on IRS Form 1040.", required=False)
    student_exemptions = forms.IntegerField(label="Enter your exemptions from 2015.", min_value=0, help_text="You can find this on line 6d of IRS Form 1040.", required=False)

    # "Did you have any of the following items in 2015? Check all that apply and list amounts."
    # " 2015 additional financial information:"
    # @maybe: DRY this out.
    student_lifetime_learning = forms.IntegerField(label="American Opportunity tax credit or Lifetime Learning tax credit", required=False)
    student_child_support_paid = forms.IntegerField(label="Child support paid", required=False)
    student_work_study_earned = forms.IntegerField(label="Taxable earnings from work-study programs, assistantships, or fellowships", required=False)
    student_grants_and_scholarships = forms.IntegerField(label="College grant or scholarship aid reported to the IRS", required=False)
    student_combat_pay = forms.IntegerField(label="Combat pay or special combat pay", required=False)
    student_coop_education = forms.IntegerField(label="Cooperative education program earnings", required=False)

    # "2015 untaxed income:"
    # @maybe: DRY this out.
    student_tax_deferred = forms.IntegerField(label="Payments to tax-deferred pension and retirement savings plans", min_value=0, required=False)
    student_ira_deductions = forms.IntegerField(label="IRA deductions and payments to self-employed SEP, SIMPLE, and Keogh", min_value=0, required=False)
    student_child_support_received = forms.IntegerField(label="Child support you received", min_value=0, required=False)
    student_interest_income = forms.IntegerField(label="Tax-exempt interest income", min_value=0, required=False)
    student_untaxed_distributions = forms.IntegerField(label="Untaxed portions of IRA distributions", min_value=0, required=False)
    student_living_allowances = forms.IntegerField(label="Housing, food, and other living allowances paid to military and clergy members", min_value=0, required=False)
    student_veterans_benefits = forms.IntegerField(label="Veterans noneducation benefits", min_value=0, required=False)
    student_other_untaxed_income = forms.IntegerField(label="Other untaxed income that’s not reported, such as workers' compensation or disability benefits", min_value=0, required=False)

    student_assets = forms.ChoiceField(choices=YES_NO_MAYBE, label="As of today, do you have more than $7,000 in assets?", help_text="Assets include bank accounts and investments.", required=False)
    # @question: Would they really want us to include things like the value
    # of a car? Irrelevant for purposes of user testing, but it's surprising.


class FAFSAApplicationForm8(forms.Form):
    # "Sign and submit"
    who_filled_this_out = forms.ChoiceField(choices=FORM_FILLER, label="Are you the student applying for financial aid, or are you a preparer?", help_text="A preparer is someone completing the FAFSA on behalf of the student, not the student themselves.", required=False)
    #signing_ssn = localflavor.USSocialSecurityNumberField(label="Social Security number", required=False)
    #signining_dob = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)', required=False)
    signing_ssn = forms.CharField(label="Social Security number", required=False)
    signining_dob = forms.CharField(label='Date of birth (MM/DD/YYYY)', required=False)

#class FAFSAApplicationForm14(forms.Form):
    # You’re almost done! To sign your FAFSA electronically, you’ll need to
    # provide some personal information to verify that you are who you say you
    # are. This helps protect you against identity theft and fraud.

    # Social Security Number
    # Last name
    # Date of birth

    # @question: We already have this data. For what do we need this?
