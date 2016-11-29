from django.shortcuts import render_to_response
from .forms import *
from formtools.wizard.views import SessionWizardView


class USCISWizard(SessionWizardView):
    template_name = "uscis_form.html"

    content = {
        '0': {
            'hed': 'Application for Naturalization',
            'subhead': '1. Basis for eligibility',
            'intro': ('In this section we will tell you the basis of eligibility'
                      ' that most closely matches the information you provide '
                      'by asking you about the following: '
                      '[...]'),
            'body': 'At the end of this section, you will be able to confirm '
                    'that the basis of eligibility presented applies to you, '
                    'or you can select a different basis of eligibility.'
        },
        '1': {
            'subhead': '2. About you',
            'intro': ('In this section, we will collect some basic information '
                      'about you, including how to contact you, your education '
                      'and employment history, details about your family, and '
                      'more.')
        },
        '2': {
            'subhead': '3. Moral character',
            'intro': ('In this section, we will ask you questions related to '
                      'your moral character.')
        },
        '3': {
            'subhead': '4. Evidence for your application',
            'intro': ('Based on the answers you provided, we have generated an '
                      'evidence checklist for you. In this section, you will '
                      'upload the requested evidence.')
        },
        '4': {
            'subhead': '5. Review application',
            'intro': ('Please review your answers and make sure everything is '
                      'correct. If you would rather review this as a PDF, you '
                      'can download your entire Application for Naturalization.')
        },
        '5': {
            'subhead': '6. Sign and pay',
            'intro': ('These are the categories of questions we may ask you '
                      'about in this section:'),
            'body': ('* Interpreter and/or preparer information,'
                     '* Applicant signature',
                     '* Payment information')
        },
    }

    def done(self, form_list, **kwargs):
        form_data = self.process_form_data(form_list)

        return render_to_response('confirmation.html', {'form_data': form_data})

    def process_form_data(self, form_list):
        form_data = [form.cleaned_data for form in form_list]

        return form_data

#    def get_form_initial(self, step):
#        consent = self.consent_to_retrieve()
#        if step in ['5', '6'] and consent:
#            return self.dummy_data.get(step)
#        return {}

#    def consent_to_retrieve(self):
#        prev_data = self.storage.get_step_data('4') or {}
#        if prev_data.get('4-consent_to_retrieve_data') == '1':
#            return True

    #def get_template_names(self):
    #    step = self.storage.current_step
    #    return self.templates[step]

    def get_context_data(self, form, **kwargs):
        context = super(USCISWizard, self).get_context_data(form, **kwargs)
        step = self.storage.current_step
        if step in self.content:
            context.update(self.content[step])
        return context
