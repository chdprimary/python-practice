from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Clean Code by Robert "Uncle Bob" Martin says:
# Use TDD workflow, and tests should cover all ocde functionality
# Each test should test ONE thing (i.e. one assertion per test)
# Make sure tests are clean as well
# Make sure tests are FIRST:
#   Fast, Independent, Repeatable, Self-validating, timely (written just before code)

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')