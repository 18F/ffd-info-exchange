from django.core.urlresolvers import resolve
from django.test import TestCase
from fafsa.views import fafsa_form


class FAFSAFormTest(TestCase):

    def test_url_resolves_to_fafsa_form_view(self):
        found = resolve('/')
        self.assertEqual(found.func, fafsa_form)
