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

        # Alice sees a table showing the historical BTC price data
        # Each row contains a datetime, price(USD), open, high, low, and percent change column
        table = self.browser.find_element_by_id('btc_data_table')
        cells = table.find_elements_by_tag_name('td')
        self.assertIn('Price', [cell.text for cell in cells])
        self.fail('Write new functional test!')

        # Alice refreshes the page and notices that the table updates

        # Alice sees a chart, above the table, plotting USD price per BTC with respect to time

if __name__ == '__main__':
    unittest.main()