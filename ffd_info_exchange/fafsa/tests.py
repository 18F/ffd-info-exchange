from django.test import TestCase


class SmokeTest(TestCase):

    def test_expected_fail(self):
        self.assertEqual(1 + 1, 5)
