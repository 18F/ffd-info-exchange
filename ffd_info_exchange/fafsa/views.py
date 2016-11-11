from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import *
from formtools.wizard.views import SessionWizardView

class FAFSAWizard(SessionWizardView):
    template_name = "fafsa_form.html"

    dummy_data = {
        '5': {
            'student_agi': 38750,
            'student_earned': 42000,
            'student_is_dislocated': '0',
            #'student_received_benefits': ['snap'],
            'student_eligible_for_simpler': '0'
        },
        '6': {
            'student_tax_paid': 9675,
            'student_exemptions': 1,
            'student_lifetime_learning': 0,
            'student_child_support_paid': 0,
            'student_work_study_earned': 0,
            'student_grants_and_scholarships': 0,
            'student_combat_pay': 0,
            'student_coop_education': 0,
            'student_tax_deferred': 0,
            'student_ira_deductions': 0,
            'student_child_support_received': 0,
            'student_interest_income': 0,
            'student_untaxed_distributions': 0,
            'student_living_allowances': 0,
            'student_veterans_benefits': 0,
            'student_other_untaxed_income': 0,
        }
    }

    templates = {
        '0': 'demographics.html',
        '1': 'contact.html',
        '2': 'eligibility.html',
        '3': 'dependents.html',
        '4': 'consent.html',
        '5': 'tax_info.html',
        '6': 'tax_info_2.html',
        '7': 'sign_and_submit.html'
    }

    content = {
        '0': {
            'hed': 'Welcome to the FAFSA!',
            'subhead': 'Your demographic information',
            'intro': ('To complete this form and be considered for federal '
                      'financial aid, you’ll need to answer a series of '
                      'questions about yourself, your parents, and your '
                      'financial history.'),
            'body': 'To begin, please share the following information:'
        },
        '1': {
            'subhead': 'Your contact information'
        },
        '2': {
            'subhead': 'Your eligibility information',
            'intro': 'Please answer these questions to help us determine whether you’re eligible for financial aid.'
        },
        '3': {
            'subhead': 'Your dependents',
            'intro': 'Share information about your dependents to help us calculate the right amount of aid for you.'
        },
        '4': {
            'subhead': 'Your tax information'
        },
        '5': {
            'subhead': 'Your tax information, continued'
        },
        '6': {
            'subhead': 'Your tax information, continued'
        },
        '7': {
            'subhead': 'Sign and submit',
            'intro': ('You\'re almost done! To sign your FAFSA electronically, '
                     'you’ll need to re-enter some personal information, which '
                     'will act as your electronic signature.')
        }
    }

    def done(self, form_list, **kwargs):
        form_data = self.process_form_data(form_list)

        return render_to_response('confirmation.html', {'form_data': form_data})

    def process_form_data(self, form_list):
        form_data = [form.cleaned_data for form in form_list]

        return form_data

    def get_form_initial(self, step):
        consent = self.consent_to_retrieve()
        if step in ['5', '6'] and consent:
            return self.dummy_data.get(step)
        return {}

    def consent_to_retrieve(self):
        prev_data = self.storage.get_step_data('4') or {}
        if prev_data.get('4-consent_to_retrieve_data') == '1':
            return True

    #def get_template_names(self):
    #    step = self.storage.current_step
    #    return self.templates[step]

    def get_context_data(self, form, **kwargs):
        context = super(FAFSAWizard, self).get_context_data(form, **kwargs)
        step = self.storage.current_step
        if step in self.content:
            context.update(self.content[step])
        return context
