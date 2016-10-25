from django.core.urlresolvers import resolve
from django.test import TestCase
from fafsa.views import fafsa_form


class FAFSAFormTest(TestCase):

    def test_url_resolves_to_fafsa_form_view(self):
        found = resolve('/')
        self.assertEqual(found.func, fafsa_form)

    def test_fafsa_form_returns_correct_html(self):
        request = HttpRequest()
        response = fafsa_form(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>FAFSA</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
