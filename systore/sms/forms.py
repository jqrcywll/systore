from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['goods_name', 'barcode', 'pic', 'num', 'input_price', 'sale_price',
                  'warehouse', 'trade_mark', 'goods_class', 'spec',]
