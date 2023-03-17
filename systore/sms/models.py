from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=64)


class GoodsClass(models.Model):
    class0 = models.CharField(max_length=16)
    class1 = models.CharField(max_length=32)


class Stock(models.Model):
    name = models.CharField(max_length=64)
    barcode = models.CharField(max_length=13)
    num = models.IntegerField(default=0)
    input_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.PROTECT, default=0)
    trade_mark = models.CharField(max_length=64, default='')
    class1_id = models.ForeignKey(GoodsClass, on_delete=models.PROTECT, default=0)
    spec = models.CharField(max_length=64, null=True)
    is_on_sale = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_filed = models.BooleanField(default=False)
    

