"""ffd_info_exchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from fafsa.forms import (FAFSAApplicationForm1,
                         FAFSAApplicationForm2,
                         FAFSAApplicationForm3,
                         FAFSAApplicationForm4,
                         FAFSAApplicationForm5,
                         FAFSAApplicationForm6,
                         FAFSAApplicationForm7,
                         FAFSAApplicationForm8)
from fafsa.views import FAFSAWizard

from uscis.forms import (N400YourEligibility,
                         N400AboutYou,
                         N400AboutYouContinued,
                         N400YourFamily,
                         N400MoralCharacter,
                         N400SignAndSubmit,
                         )
from uscis.views import (USCISWizard,
                         select_bonus_services,
                         get_name_change_form,
                         get_global_entry_form,
                         get_passport_form,
                         confirm_name_change_application,
                         confirm_passport_application,
                         confirm_global_entry_application,
                         )

urlpatterns = [
    url(r'^fafsa/$', FAFSAWizard.as_view([FAFSAApplicationForm1,
                                          FAFSAApplicationForm2,
                                          FAFSAApplicationForm3,
                                          FAFSAApplicationForm4,
                                          FAFSAApplicationForm5,
                                          FAFSAApplicationForm6,
                                          FAFSAApplicationForm7,
                                          FAFSAApplicationForm8])),
    # Setting USCIS as the new default. Could change it to `uscis` later.
    url(r'^$', USCISWizard.as_view([N400YourEligibility,
                                    N400AboutYou,
                                    N400AboutYouContinued,
                                    N400YourFamily,
                                    N400MoralCharacter,
                                    N400SignAndSubmit,
                                    ])),
    url(r'^select-bonus-services', select_bonus_services, name='bonus-services'),
    url(r'^name-change', get_name_change_form, name='name-change'),
    url(r'^confirm-name-change-application', confirm_name_change_application, name='confirm-name-change'),
    url(r'^global-entry', get_global_entry_form, name='global-entry'),
    url(r'^confirm-global-entry-application', confirm_global_entry_application, name='confirm-global-entry'),
    url(r'^passport', get_passport_form, name='passport'),
    url(r'^confirm-passport', confirm_passport_application, name='confirm-passport'),
]
