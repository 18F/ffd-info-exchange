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
#from django.contrib import admin

from fafsa.forms import FAFSAApplicationForm1, FAFSAApplicationForm2, FAFSAApplicationForm3, FAFSAApplicationForm4, FAFSAApplicationForm5, FAFSAApplicationForm6, FAFSAApplicationForm7, FAFSAApplicationForm8, FAFSAApplicationForm9, FAFSAApplicationForm10
from fafsa.views import FAFSAWizard

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', FAFSAWizard.as_view([FAFSAApplicationForm1, FAFSAApplicationForm2, FAFSAApplicationForm3, FAFSAApplicationForm4, FAFSAApplicationForm5, FAFSAApplicationForm6, FAFSAApplicationForm7, FAFSAApplicationForm8, FAFSAApplicationForm9, FAFSAApplicationForm10])),
]
