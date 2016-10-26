from .models import Application
import floppyforms.__future__ as forms


class FAFSAApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name_first', 'name_last', 'date_of_birth']
