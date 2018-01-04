from django.shortcuts import render, redirect
from bitcoinchart.models import Order

import os
import csv

def home_page(request):
    if request.method == 'POST':
        Order.objects.create(amount=request.POST['order_amount'])
        return redirect('/')

    FILE_PATH = os.path.join('bitcoinchart', 'datasets')
    FILE_NAME = os.path.join('practice_btc_historical_data.csv')
    hist_data = None
    with open(os.path.join(FILE_PATH , FILE_NAME)) as fileobj:
        readerobj = csv.reader(fileobj)
        hist_data = list(readerobj)

    orders = Order.objects.all()

    return render(request, 'home.html', {
        'rows': hist_data,
        'orders': orders,
    })