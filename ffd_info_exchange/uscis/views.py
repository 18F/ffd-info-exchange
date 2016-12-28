from django.shortcuts import render, render_to_response
from .forms import *
from formtools.wizard.views import SessionWizardView

bonuses_completed = {'name_change': False,
                     'global_entry': False,
                     'passport': False,
                     }

# Working off of http://django-formtools.readthedocs.io/en/latest/wizard.html#wizard-template-for-each-form.
# Note: these currently get cranky when given non-numeric keys. :(
# @todo: Update name to clarify that these are N400 steps, which != all forms.
FORMS = [('0', N400YourEligibility),
         ('1', N400AboutYou),
         ('2', N400AboutYouContinued),
         ('3', N400YourFamily),
         ('4', N400MoralCharacter),
         ('5', N400SignAndSubmit),
         ]

# @todo: DRY.
TEMPLATES = {'0': 'n400-default.html',
             '1': 'n400-default.html',
             '2': 'n400-default.html',  # @todo: Break out the form fields into groupings.
             '3': 'n400-default.html',
             '4': 'n400-default.html',
             '5': 'n400-sign-and-pay.html',
             }


# @todo: Follow the 'pay_by_credit_card' example when setting up whether they
# want to pursue more options. [#108]


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
            'subhead': '3. Information about you, continued',
        },
        '3': {
            'subhead': '4. Information about your family',
            'intro': ('Share the following information about your family to '
                      'help us better understand your eligibility for '
                      'citizenship.')
        },
        '4': {
            'subhead': '5. Moral character',
            'intro': ('In this section, we’ll ask you questions related to '
                      'your moral character.')
        },
        '5': {
            'subhead': '6. Sign and submit',
            # @todo: If time allows, add signature-in-place functionality for
            # the "Applicant's signature" and "Translator's signature (if
            # applicable)"
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


def select_bonus_services(request):
    return render(request, 'select-bonus-services.html', {'bonuses_completed': bonuses_completed})


# @todo: DRY this out.
def get_name_change_form(request):
    form = NameChange()

    return render(request, 'name-change.html', {'form': form})


def get_global_entry_form(request):
    form = GlobalEntry()

    return render(request, 'global-entry.html', {'form': form})


def get_passport_form(request):
    form = Passport()

    return render(request, 'passport.html', {'form': form})


# @todo: DRY this out.
def confirm_name_change_application(request):
    bonuses_completed['name_change'] = True
    return render(request, 'confirmation-name-change.html')


def confirm_global_entry_application(request):
    bonuses_completed['global_entry'] = True
    return render(request, 'confirmation-global-entry.html')


def confirm_passport_application(request):
    bonuses_completed['passport'] = True
    return render(request, 'confirmation-passport.html')
