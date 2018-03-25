from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_view_returns_correct_html(self):
        # this 'self.client' is the *django test client*
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_view_can_handle_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('1: A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')