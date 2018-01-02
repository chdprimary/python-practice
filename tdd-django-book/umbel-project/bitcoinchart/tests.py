from django.test import TestCase

import os
import csv

# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_dataset_file_loaded(self):
        FILE_PATH = os.path.join('bitcoinchart', 'datasets')
        FILE_NAME = 'practice_btc_historical_data.csv'
        response = self.client.get('/')
        with open(os.path.join(FILE_PATH, FILE_NAME)) as file_obj:
            reader_obj = csv.reader(file_obj)
            contents = list(reader_obj)
            for row in contents:
                for cell in row:
                    self.assertIn(cell, response.content.decode())