from django.urls import path
from . import views

app_name = 'sms'

urlpatterns = [
    path('', views.index, name='index'),

    path('stock/', views.stock, name='stock'),
    path('stock/add', views.stock_add, name='stockadd'),

    path('bill/', views.bill, name='bill'),
    # path('analysis/', views.analysis, name='analysis'),
]
