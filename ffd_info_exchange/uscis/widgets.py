from django import forms
from django.utils.html import format_html

class LabelInputSiblingRenderer():
    def render(self, name=None, value=None, attrs=None):
        # This is mostly just a copy-paste of our superclass method, it
        # just tweaks the HTML structure to be USWDS-friendly.
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            raise ValueError('USWDS-style inputs must have "id" attributes')
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        return format_html(
            '{}<label{}>{}</label>', self.tag(attrs), label_for,
            self.choice_label,
        )


class UswdsCheckboxInput(LabelInputSiblingRenderer,
                         forms.widgets.CheckboxChoiceInput):
    pass


class UswdsRadioChoiceInput(LabelInputSiblingRenderer,
                            forms.widgets.RadioChoiceInput):
    pass


class UswdsRadioFieldRenderer(forms.widgets.ChoiceFieldRenderer):
    choice_input_class = UswdsRadioChoiceInput


class UswdsRadioSelect(forms.widgets.RadioSelect):
    renderer = UswdsRadioFieldRenderer


class UswdsCheckboxFieldRenderer(forms.widgets.ChoiceFieldRenderer):
    choice_input_class = UswdsCheckboxInput


class UswdsCheckbox(forms.widgets.CheckboxSelectMultiple):
    renderer = UswdsCheckboxFieldRenderer
