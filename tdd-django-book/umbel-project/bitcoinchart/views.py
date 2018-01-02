from django.shortcuts import render
import os
import csv

def home_page(request):
    FILE_PATH = os.path.join('bitcoinchart', 'datasets')
    FILE_NAME = os.path.join('practice_btc_historical_data.csv')
    btc_data = None
    with open(os.path.join(FILE_PATH , FILE_NAME)) as fileobj:
        readerobj = csv.reader(fileobj)
        btc_data = list(readerobj)

    return render(request, 'home.html', {
        'rows': btc_data
    })