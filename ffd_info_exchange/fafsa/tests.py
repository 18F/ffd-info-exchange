from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from fafsa.views import fafsa_form


class FAFSAFormTest(TestCase):

    def test_url_resolves_to_fafsa_form_view(self):
        found = resolve('/')
        self.assertEqual(found.func, fafsa_form)

    def test_fafsa_form_returns_correct_html(self):
        request = HttpRequest()
        response = fafsa_form(request)
        expected_html = render_to_string('fafsa_form.html')
        self.assertEqual(response.content.decode(), expected_html)
