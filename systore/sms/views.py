from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
import gettext as _

from .models import Stock
from .forms import StockForm


def index(request):
    return render(request, 'sms/index.html')


def stock(request):
    stocks = Stock.objects.order_by('time_created')
    context = {'stocks': stocks}
    return render(request, 'sms/stock.html', context)


def stock_add(request):
    if request.method != 'POST':
        form = StockForm()
    else:
        print('POST DATA', request.POST)
        form = StockForm(request.POST)
        if form.is_valid():
            print(1234556)
            # form.save()
            return HttpResponseRedirect(reverse('sms:stock'))
        else:
            raise ValidationError("sdfsffsfd")
    context = {'form': form}
    return render(request, 'sms/stock_add.html', context)


def bill(request):
    return render(request, 'sms/bill.html')
