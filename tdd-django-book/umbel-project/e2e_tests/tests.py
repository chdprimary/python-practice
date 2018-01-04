from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_home_page_and_submit_an_order(self):
        # Alice goes to our app's homepage URI and a page loads
        self.browser.get(self.live_server_url)

        # Alice notices that the browser title reads 'Bitcoin Chart'
        # Alice notices that the page header reads 'Bitcoin Price'
        self.assertIn('Bitcoin Chart', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bitcoin Price', header_text)

        # Alice sees a header reading 'BTC Historical Data'
        header_text = self.browser.find_element_by_id('historical_data_header').text
        self.assertIn('BTC Historical Data', header_text)

        # Alice sees a table showing the historical BTC price data
        # Each row contains a datetime, price(USD), open, high, low, and percent change column
        hist_table = self.browser.find_element_by_id('historical_data_table')
        rows = hist_table.find_elements_by_tag_name('tr')
        self.assertIn('Price', rows[0].text)

        # Alice sees a header reading 'Place Order'
        header_text = self.browser.find_element_by_id('btc_order_header').text
        self.assertIn('Place Order', header_text)

        # Alice sees a form, below the header, for placing buy/sell market orders
        select_box = self.browser.find_element_by_id('order_type_selector')
        options = select_box.find_elements_by_tag_name('option')
        self.assertEqual(len(options), 2)

        # Alice submits an order and notices that the order item appears in a table below
        inputbox = self.browser.find_element_by_id('order_amount_field')
        inputbox.send_keys('100.00')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        order_table = self.browser.find_element_by_id('order_table')
        rows = order_table.find_elements_by_tag_name('tr')
        self.assertEqual(len(rows), 2)
        self.assertIn('100.00', rows[1].text)

        # Alice refreshes the page and notices that the historical data table updates
        self.fail('Write new functional test!')

        # Alice sees a chart, above the table, plotting USD price per BTC with respect to time
