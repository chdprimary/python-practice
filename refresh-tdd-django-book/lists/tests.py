from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_view_returns_correct_html(self):
        # this 'self.client' is the *django test client*
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')