from django.shortcuts import render_to_response
from .forms import *
from formtools.wizard.views import SessionWizardView

# Working off of http://django-formtools.readthedocs.io/en/latest/wizard.html#wizard-template-for-each-form.
# Note: these currently get cranky when given non-numeric keys. :(
FORMS = [('0', N400Step1),
         ('1', N400Step2),
         ('2', N400Step3),
         ('3', N400Step4),
         ('4', N400Step5),
         ('5', N400Step6),
         ('6', N400Step7),
         ('7', AdditionalServices),
         ('8', NameChange),
         ('9', TSAPreCheck),
         ('10', Passport),
         ]

TEMPLATES = {'0': 'n400-default.html',
             '1': 'n400-default.html',
             '2': 'n400-default.html',
             '3': 'n400-default.html',
             '4': '5-n400.html',
             '5': 'n400-default.html',
             '6': 'n400-sign-and-pay.html',
             '7': 'select-bonus-services.html',
             '8': 'name-change.html',
             '9': 'tsa.html',
             '10': 'passport.html'
             }


# @todo: Follow the 'pay_by_credit_card' example when setting up whether they
# want to pursue more options.


class USCISWizard(SessionWizardView):
    content = {
        '0': {
            'hed': 'Application for Naturalization',
            'subhead': '1. Information about your eligibility',
            'intro': ('Please provide some information to help us determine '
                      'whether you’re eligible to apply for U.S. citizenship.'),
        },
        '1': {
            'subhead': '2. Information about you',
            'intro': ('Thanks for sharing your eligibility information. '
                      'Now we’d like to ask you for some information about '
                      'yourself.')
        },
        '2': {
            'subhead': '3. Information about your family',
            'intro': ('Share the following information about your family to '
                      'help us better understand your eligibility for '
                      'citizenship.')
        },
        '3': {
            'subhead': '4. Moral character',
            'intro': ('In this section, we’ll ask you questions related to '
                      'your moral character.')
        },
        '4': {
            'subhead': '5. Evidence for your application',
            'intro': ('Now that you’ve provided all the required information '
                      'about yourself, please upload scanned copies of the '
                      'following documents: '),
            'body': ('* Your birth certificate'
                     '* Your Permanent Resident Card (green card)'
                     '* Your driver’s license'
                     '* Your most recent tax return'
                     '* Two identical photographs (color, passport-style)'
                     '* If you’re married: A copy of your marriage certificate'
                     )
            },
        '5': {
            'subhead': '6. Review your application',
            'intro': ('Please review your answers and make sure everything is '
                      'correct. If you would rather review your application as '
                      'a PDF, you can download the entire form.')
        },
        '6': {
            'subhead': '7. Sign and pay',
            # @todo: If time allows, add signature-in-place functionality for
            # the "Applicant's signature" and "Translator's signature (if
            # applicable)"
        },
        # @todo: As part of #130, refactor these into separate forms entirely.
        '8': {
            'subhead': 'Name change (optional)',
            'intro': ("You indicated that you’d like to legally change your "
                      'name. Please provide your desired new name in the fields '
                      'below.'),
            'body': ('Once your Application for Naturalization is approved, '
                     'your name change request will be processed. If your '
                     'Application for Naturalization is not approved, your '
                     'name change request will not be granted.')
        },
        '9': {
            'subhead': 'Global Entry/TSA PreCheck application (optional)',
            'intro': ('You indicated that you’d like to apply for Global Entry/'
                      'TSA PreCheck. You’ve already provided most of the '
                      'information necessary for this application; you’ll need '
                      'to answer just a few additional questions.'),
            'body': ('Additional information:')
        },
        '10': {
            'subhead': 'U.S. passport application (optional)',
            'intro': (''),
            'body': ('')
        },
    }

    def done(self, form_list, **kwargs):
        form_data = self.process_form_data(form_list)

        return render_to_response('select-bonus-services.html', {'form_data': form_data})

    def process_form_data(self, form_list):
        form_data = [form.cleaned_data for form in form_list]

        return form_data

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super(USCISWizard, self).get_context_data(form, **kwargs)
        step = self.storage.current_step
        if step in self.content:
            context.update(self.content[step])
        return context
