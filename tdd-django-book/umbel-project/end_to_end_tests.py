from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_home_page(self):
        # Alice navigates to 'localhost:8000' and a page loads
        self.browser.get('http://localhost:8000')
        # Alice notices that the browser title reads 'Bitcoin Chart'
        # Alice notices that the page header reads 'Bitcoin Price'
        self.assertIn('Bitcoin Chart', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bitcoin Price', header_text)

    def test_bitcoin_historical_data_displayed_in_table(self):
        self.fail('Do more tests!')

if __name__ == '__main__':
    unittest.main()