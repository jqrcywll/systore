from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'barcode', 'num', 'input_price', 'sale_price',
                  'warehouse_id', 'trade_mark', 'class1_id', 'spec',]
        labels = {
            'name': '商品名',
            'barcode': '条码',
            'num': '数量',
            'input_price': '进货价',
            'sale_price': '零售价',
            'warehouse_id': '货架号',
            'trade_mark': '品牌',
            'class1_id': '品类',
            'spec': '规格',
        }
