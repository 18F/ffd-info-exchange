from localflavor.us import forms as localflavor
from localflavor.us.forms import USSocialSecurityNumberField, USStateSelect, USZipCodeField, USPSSelect, USPhoneNumberField
from django import forms
#import floppyforms.__future__ as floppyforms

YES_OR_NO = (('1', 'Yes'), ('0', 'No'))
YES_NO_MAYBE = (('1', 'Yes'), ('0', 'No'), ('2', 'Maybe'))
GENDER_OPTIONS = (('female', 'Female'), ('male', 'Male'))
MARITAL_STATUS = (('single', 'Single'), ('married_or_remarried', 'Married or remarried'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('widowed', 'Widowed'))
CITIZENSHIP_STATUS = (('yes', "Yes, I'm a U.S. citizen (or U.S. national)"), ('no_but_eligible', "No, but I'm an eligible noncitizen"), ('not_at_all', "No, I'm not a citizen or eligible noncitizen"))
SCHOOL_COMPLETION_STATUS = (('diploma', "I’ll have a high school diploma"), ('ged', "I’ll have a GED certificate or state-authorized high school equivalent certificate"), ('home_schooled', "I was home schooled and will have completed my curriculum"), ('none', "None of the above"))
COLLEGE_GRADE_LEVEL = (('0', "First-year student (never attended college)"), ('1', "First-year student (attended college before)"), ('2', "Second-year student (sophomore)"), ('3', "Third-year student (junior)"), ('4', "Fourth-year student (senior)"), ('5', "Fifth-year student (other undergraduate)"), ('6', "First-year graduate/professional student"), ('grad_continuing', "Continuing graduate/professional student/beyond"))
DEGREES = (('1', "First bachelor’s degree"), ('2', "Second bachelor’s degree"), ('3', "Associate degree (occupational or technical program)"), ('4', "Associate degree (general education/transfer program)"), ('5', "Certificate/diploma (occupational/technical/educational program of less than two years)"), ('6', "Certificate/diplomat (occupational/technical/educational program of at least two years)"), ('7', "Teaching credential program (nondegree)"), ('8', "Graduate or professional degree"), ('9', "Other or undecided"))
PARENTS_SCHOOL_COMPLETION = (('middle'), ("Middle school/junior high")), (('high'), ("High school")), (('college'), ("College or beyond")), (('not_sure'), ("I don’t know")),
HOUSING_PLANS = (('on_campus', "On campus"), ('parents', "With parent(s)"), ('off_campus', "Off campus"))
MARITAL_STATUS_PARENTS = (('never_married', "Never married"), ('live_together', "Unmarried and both parents living together"), ('married', "Married or remarried"), ('divorced', "Divorced or separated"), ('widowed', "Widowed"))
TAX_COMPLETION_STATUS = (('already_filed', "They’ve already completed it"), ('will_file', "They will file it"), ('wont_file', "They’re not going to file it"))
TAX_FILING_STATUS = (('single', "Single"), ('head', "Head of household"), ('joint', "Married — filed joint return"), ('separate', "Married — filed separate returns"), ('widowed', "Qualifying widow or widower"), ('not_sure', "I’m not sure"))
TAX_FORM_TYPES = (('1040', "IRS 1040"), ('1040a', "IRS 1040A or 1040EZ"), ('foreign', "Foreign tax return"), ('associated', "A tax return with Puerto Rico, a U.S. territory, or a freely associated state"))
BENEFIT_PROGRAMS = (('medicaid', "Medicaid"), ('ssi', "Supplemental Security Income (SSI)"), ('snap', "Supplemental Nutrition Assistance Program (SNAP)"), ('lunch', "Free or reduced-price school lunch"), ('tanf', "Temporary Assistance for Needy Families (TANF)"), ('wic', "Special Supplemental Nutrition Program for Women, Infants, and Children (WIC)"), ('none', "None of the above"))


class FAFSAApplicationForm1(forms.Form):
    # "Your demographic information" section
    # To start the application process, we'll need to collect some basic information about you.
    first_name = forms.CharField(label="First name")
    middle_initial = forms.CharField(label="Middle initial", max_length=1)
    last_name = forms.CharField(label="Last name")
    ssn = localflavor.USSocialSecurityNumberField(label="Social Security number", help_text="Why do we need this? We collect your Social Security number to verify your identity and protect you against fraud. We don’t store this information once we’ve processed your FAFSA.")
    date_of_birth = forms.DateTimeField(label='Date of birth (MM/DD/YYYY)')
    assigned_sex = forms.ChoiceField(choices=GENDER_OPTIONS, label="What gender were you designated at birth?")
    mailing_address_permanent = forms.CharField(label="Permanent mailing address (incl. apt number)")
    mailing_address_city = forms.CharField(label="City")
    mailing_address_country = forms.CharField(label="Country, if not U.S.", required=False)  # @todo: Incorporate localflavor
    mailing_address_state = localflavor.USStateSelect()  # @todo: Fix this.
    mailing_address_zip = localflavor.USZipCodeField(label="ZIP code")
    state_five_years = forms.ChoiceField(choices=YES_OR_NO, label="Have you lived in your state for at least five years?")
    usps = localflavor.USPSSelect()  # @todo: Determine whether this is relevant.
    phone = localflavor.USPhoneNumberField(label="Telephone number")
    email = forms.EmailField(label="Email address")
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="Current marital status")
    drivers_license = forms.ChoiceField(choices=YES_OR_NO, label="Do you have driver's license information that you'd like to share?")
    # @todo: Add conditional driver's license number.
    # @todo: Add conditional driver's license state (dropdown select).


class FAFSAApplicationForm2(forms.Form):
    # "Your financial aid eligibility" section
    # Please answer these questions to help us determine whether you’re eligible for financial aid.
    us_citizen = forms.ChoiceField(choices=CITIZENSHIP_STATUS, label="Are you a U.S. citizen?")
    high_school_status = forms.ChoiceField(choices=SCHOOL_COMPLETION_STATUS, label="What will your high school completion status be when you begin college in the 2017-2018 school year?")
    entering_grade_level = forms.ChoiceField(choices=COLLEGE_GRADE_LEVEL, label="What will your college grade level be when you begin the 2017-2018 school year?")
    degree_pursued = forms.ChoiceField(choices=DEGREES, label="What degree or certificate will you be working on when you begin the 2017-2018 school year?")
    work_study = forms.ChoiceField(choices=YES_NO_MAYBE, label="Would you like to be considered for work study?")
    has_degree = forms.ChoiceField(choices=YES_OR_NO, label="Will you have your first bachelor's degree before you begin the 2017-2018 school year?")
    foster_youth = forms.ChoiceField(choices=YES_OR_NO, label="Are you a foster youth, or were you ever in the foster care system?")
    completed_parent_1 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 1")
    completed_parent_2 = forms.ChoiceField(choices=PARENTS_SCHOOL_COMPLETION, label="Highest school completed by Parent 2")


class FAFSAApplicationForm3(forms.Form):
    # "Your financial aid eligibility, continued" section
    high_school_name = forms.CharField(label="What is the name of your high school?")
    high_school_city = forms.CharField(label="In what city is your high school?")
    # @todo: Fix this next one. label="In what state is your high school?"
    high_school_state = localflavor.USStateSelect()


class FAFSAApplicationForm4(forms.Form):
    # "School selection" section
    # @TODO: Flesh this out.
    # "You can send your completed FAFSA to up to four schools free of charge; you can send it to additional schools for a small fee."
    # "For each of the four schools to which you’d like to send the FAFSA, enter the school code (if you know it). If you don’t know it, look up each school by name or location (city and state)."
    school_code = forms.CharField(label="For each of the four schools to which you’d like to send the FAFSA, enter the school code (if you know it).")


class FAFSAApplicationForm5(forms.Form):
    # "School selection summary" section
    housing_plans = forms.ChoiceField(choices=HOUSING_PLANS, label="Add housing plans")


class FAFSAApplicationForm6(forms.Form):
    # "Dependency determination" section
    has_dependents_children = forms.ChoiceField(choices=YES_OR_NO, label="Do you now have or will you have children who will receive more than half of their support from you between July 1, 2017 and June 30, 2018?")
    has_dependents_non_children = forms.ChoiceField(choices=YES_OR_NO, label="Do you have dependents (other than your children or spouse) who live with you and who receive more than half of their support from you, now and through June 30, 2018?")
    household_size = forms.IntegerField(label="Your number of household members in 2017-2018", min_value=1)
    num_household_college = forms.IntegerField(label="How many people in your household will be in college in 2017-2018?", min_value=0)
    qs_about_parents = forms.ChoiceField(choices=YES_OR_NO, label="Do you want to answer questions about your parents?")


class FAFSAApplicationForm7(forms.Form):
    # "Parent demographics information" section
    marital_status_parents = forms.ChoiceField(choices=MARITAL_STATUS_PARENTS, label="As of today, what is the marital status of your legal parents (biological and/or adoptive)?")
    parent_1_ssn = USSocialSecurityNumberField(label="What is this parent's Social Security number?")
    parent_1_last_name = forms.CharField(label="What is this parent's last name?")
    parent_1_first_initial = forms.CharField(label="What is this parent's first initial?")
    parent_1_date_of_birth = forms.DateTimeField(label="What is this parent's date of birth?", help_text="(MM/DD/YYYY)")
    parent_1_email = forms.EmailField(label="What is this parent's email address?")
    parent_1_state_five_years = forms.ChoiceField(choices=YES_OR_NO, label="Has this parent lived in their current state for at least five years?")
    parent_1_household_size = forms.IntegerField(label="Your parent's number of household members in 2017-2018", min_value=1)
    parent_1_num_household_college = forms.IntegerField(label="How many people in this parent's household will be in college between July 1, 2017 and June 30, 2018? Do not include your parents.", min_value=0)


class FAFSAApplicationForm8(forms.Form):
    # "Parent tax information" section
    # To determine your eligibility for federal financial aid, we’ll need to ask you a few questions about your parent’s (or parents’) tax information.
    parents_taxes_completed = forms.ChoiceField(choices=TAX_COMPLETION_STATUS, label="Have your parents completed their 2015 IRS income tax return or another tax return?")
    parents_filing_status = forms.ChoiceField(choices=TAX_FILING_STATUS, label="For 2015, what is your parents' tax filing status (according to their tax return)?")


class FAFSAApplicationForm9(forms.Form):
    # "Parent financial information" section
    # "We have a few more questions about your parents' income and tax information."
    parents_return_type = forms.ChoiceField(choices=TAX_FORM_TYPES, label="What type of income tax return did your parents file for 2015?")
    parents_agi = forms.IntegerField(label="What was your parents’ adjusted gross income for 2015?", min_value=0, help_text="You can find this number on IRS Form 1040, line 37.")
    parent_1_earned = forms.IntegerField(label="How much did your first parent earn from working (including wages, salaries, and tips) in 2015?", min_value=0, help_text="Calculate this by adding lines 7, 12, and 18 of the IRS Form 1040.")
    parent_2_earned = forms.IntegerField(label="How much did your second parent earn from working (including wages, salaries, and tips) in 2015?", min_value=0, help_text="Calculate this by adding lines 7, 12, and 18 of the IRS Form 1040.")
    parent_is_dislocated = forms.ChoiceField(choices=YES_NO_MAYBE, label="As of today, is either of your parents a dislocated worker?")
    received_benefits = forms.MultipleChoiceField(choices=BENEFIT_PROGRAMS, label="In 2015 or 2016, did you, your parents, or anyone in your parents’ household receive benefits from any of the federal programs listed below? Check all that apply or check 'None of the above' if, at the time you are completing the FAFSA, you, your parents, or anyone in your parents’ household did NOT receive any of these benefits during 2015 or 2016, but will receive any of them on or before December 31, 2016, you must return to the FAFSA and update your response.", help_text="Please note that answering these questions won’t impact your eligibility for these programs or student aid.")
    eligible_for_simpler = forms.ChoiceField(choices=YES_NO_MAYBE, label="You indicated that your parents filed an IRS 1040. Were they eligible to file a 1040A or 1040EZ?")


class FAFSAApplicationForm10(forms.Form):
    # "Parent financial information, continued" section
    parents_tax_paid = forms.IntegerField(label="How much income tax did your parents pay in 2015?", min_value=0, help_text="Calculate this by subtracting line 46 from line 56 on IRS Form 1040.")
    parents_exemptions = forms.IntegerField(label="Enter your parents’ exemptions from 2015.", min_value=0, help_text="You can find this on line 6d of IRS Form 1040.")

    # "Did your parents have any of the following items in 2015? Check all that apply and list amounts."
    # " 2015 additional financial information:"
    lifetime_learning = forms.IntegerField(label="American Opportunity tax credit or Lifetime Learning tax credit", required=False)
    child_support_paid = forms.IntegerField(label="Child support paid", required=False)
    work_study_earned = forms.IntegerField(label="Taxable earnings from work-study programs, assistantships, or fellowships", required=False)
    grants_and_scholarships = forms.IntegerField(label="College grant and scholarship aid reported to the IRS", required=False)
    combat_pay = forms.IntegerField(label="Combat pay or special combat pay", required=False)
    coop_education = forms.IntegerField(label="Cooperative education program earnings", required=False)

    # "2015 untaxed income:"
    tax_deferred = forms.IntegerField(label="Payments to tax-deferred pension and retirement savings plans", min_value=0, required=False)
    ira_deductions = forms.IntegerField(label="IRA deductions and payments to self-employed SEP, SIMPLE, and Keogh", min_value=0, required=False)
    child_support_received = forms.IntegerField(label="Child support your parents received", min_value=0, required=False)
    interest_income = forms.IntegerField(label="Tax-exempt interest income", min_value=0, required=False)
    untaxed_distributions = forms.IntegerField(label="Untaxed portions of IRA distributions", min_value=0, required=False)
    living_allowances = forms.IntegerField(label="Housing, food, and other living allowances paid to military and clergy members", min_value=0, required=False)
    veterans_benefits = forms.IntegerField(label="Veterans noneducation benefits", min_value=0, required=False)
    other_untaxed_income = forms.IntegerField(label="Other untaxed income that’s not reported, such as workers' compensation or disability benefits", min_value=0, required=False)

    value_accounts = forms.IntegerField(label="As of today, how much money do your parents have in cash, savings accounts, and checking accounts?", min_value=0)
    value_investments = forms.IntegerField(label="As of today, what is the net worth of your parents’ investments, including real estate?", help_text="Don’t include the value of their home.", min_value=0)
    value_businesses = forms.IntegerField(label="As of today, what is the net worth of your parents’ current businesses and/or investment farms?", help_text="Don't include a family farm or family business with 100 or fewer full-time employees.", min_value=0)
