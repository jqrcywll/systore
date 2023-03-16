from django.shortcuts import render

def index(request):
    return render(request, 'sms/index.html')

def stock(request):
    context = {
        'id': 100,
        'name': "abc",
        'barcode': '131313131313',
        'num': 17,
        'input_price': 3.14,
        'sale_price': 618.00,
        'warehouse_id': 3,
        'trade_mark': '晨光',
        'class1_id': 32,
        'spec': '0.7mm',
        'time_created': '2022-07-30 14:03:28',
    }
    return render(request, 'sms/stock.html')

def bill(request):
    return render(request, 'sms/bill.html')
