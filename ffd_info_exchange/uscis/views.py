from django.shortcuts import render_to_response
from .forms import *
from formtools.wizard.views import SessionWizardView


class USCISWizard(SessionWizardView):
    template_name = "uscis_form.html"

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
            'intro': ('I verify that all of the information I’ve included in '
                      'my application is true and correct, to the best of my '
                      'knowledge. In addition, I verify that:'),
            'body': ('* I can read and understand English and completed every question myself, OR I worked with an approved translator to complete this application.'
                     '* I’ve provided all the requested evidence to support my application.',
                     '* I’ve enclosed my biometrics fee and processing fee.')
            # @todo: Consider adding signature-in-place functionality for
            # the "Applicant's signature" and "Translator's signature (if
            # applicable)"
        },
        '7': {
            'subhead': '8. Optional recommended services',
            'intro': ("Based on the information you provided, you’re eligible "
                      "to legally change your name and apply for TSA PreCheck "
                      "and a U.S. passport."),
            'body': ('If your applications for a name change, TSA PreCheck, '
                     'and/or a U.S. passport are approved, the granting '
                     'agencies will contact you directly.')
        },
        '8': {
            'subhead': 'Name change (optional)',
            'intro': ("You indicated that you’d like to legally change your "
                      'name. Please provide your new name in the fields below.'),
            'body': ('Once your Application for Naturalization is approved, '
                     'your name-change request will be processed. If your '
                     'Application for Naturalization is not approved, your '
                     'name-change request will not be granted.')
        },
        '9': {
            'subhead': 'TSA PreCheck application (optional)',
            'intro': (''),
            'body': ('')
        },
        '10': {
            'subhead': 'U.S. passport application (optional)',
            'intro': (''),
            'body': ('')
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
