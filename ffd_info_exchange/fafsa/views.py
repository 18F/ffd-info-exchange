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
            'student_received_benefits': ['snap'],
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
