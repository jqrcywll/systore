from django.db import models

class Stock(models.Model):
    barcode = models.CharField(max_length=32)
    pic = models.CharField(max_length=512)
    brand = models.CharField(max_length=128)

    class Class_1(models.TextChoices):
        SNACK = '零食'
        STATIONERY = '文具'
        PRESENT = '礼品'
    class_1 = models.CharField(
        max_length=10,
        choices=Class_1.choices,
        default=Class_1.PRESENT,
    )
    class_2 = models.CharField(max_length=32)
    spec= models.CharField(max_length=32)
    keyword = models.CharField(max_length=128)