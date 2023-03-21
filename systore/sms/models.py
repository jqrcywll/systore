from django.db import models
from django.core.validators import MinValueValidator

class Stock(models.Model):
    goods_name = models.CharField(verbose_name='商品名', max_length=64)
    barcode = models.CharField(verbose_name='条码', max_length=13)
    pic = models.URLField(verbose_name='参考图', blank=True)
    num = models.IntegerField(verbose_name='数量', validators=[MinValueValidator(0, message='数量必须大于0'),])
    input_price = models.DecimalField(verbose_name='进货价', max_digits=7, decimal_places=2, validators=[MinValueValidator(0),])
    sale_price = models.DecimalField(verbose_name='零售价', max_digits=7, decimal_places=2)

    WAREHOUSE_A1 = 'A1'
    WAREHOUSE_A2 = 'A2'
    WAREHOUSE_A3 = 'A3'
    WAREHOUSE_CHOICES = [
        (WAREHOUSE_A1, 'A1'),
        (WAREHOUSE_A2, 'A2'),
        (WAREHOUSE_A3, 'A3'),
    ]
    warehouse = models.CharField(verbose_name='仓库', choices=WAREHOUSE_CHOICES, max_length=16, default=WAREHOUSE_A1)
    trade_mark = models.CharField(verbose_name='品牌', blank=True, max_length=64)

    GOODS_CLASS_PEN = '笔'
    GOODS_CLASS_JUICE = '饮料'
    GOODS_CLASS_CARD = '明星片'
    GOODS_CLASS_CHOICES = [
        (GOODS_CLASS_PEN, '笔'),
        (GOODS_CLASS_JUICE, '饮料'),
        (GOODS_CLASS_CARD, '明信片'),
    ]
    goods_class = models.CharField(verbose_name='品类', choices=GOODS_CLASS_CHOICES, max_length=16, default=GOODS_CLASS_PEN)
    spec = models.CharField(verbose_name='规格', blank=True, max_length=128)
    time_created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_filed = models.BooleanField(verbose_name='是否归档', default=False)
    is_on_sale = models.BooleanField(verbose_name='是否上架', default=True)
    

