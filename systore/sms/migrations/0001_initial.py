# Generated by Django 4.1.5 on 2023-03-21 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=64, verbose_name='商品名')),
                ('barcode', models.CharField(max_length=13, verbose_name='条码')),
                ('pic', models.URLField(blank=True, verbose_name='参考图')),
                ('num', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='数量必须大于0')], verbose_name='数量')),
                ('input_price', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='进货价')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='零售价')),
                ('warehouse', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')], default='A1', max_length=16, verbose_name='仓库')),
                ('trade_mark', models.CharField(blank=True, max_length=64, verbose_name='品牌')),
                ('goods_class', models.CharField(choices=[('笔', '笔'), ('饮料', '饮料'), ('明星片', '明信片')], default='笔', max_length=16, verbose_name='品类')),
                ('spec', models.CharField(blank=True, max_length=128, verbose_name='规格')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_filed', models.BooleanField(default=False, verbose_name='是否归档')),
                ('is_on_sale', models.BooleanField(default=True, verbose_name='是否上架')),
            ],
        ),
    ]
