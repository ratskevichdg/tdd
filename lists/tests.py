from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """Smoke test"""

    def test_bad_math(self):
        """test: incorrect math calculations"""
        self.assertEqual(1 + 1, 3)
