from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, request
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """Home page test"""

    def test_hame_page_returns_correct_html(self):
        """test: home page returns correct html"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
