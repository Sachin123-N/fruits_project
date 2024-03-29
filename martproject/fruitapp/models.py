from django.db import models


class Fruit(models.Model):
    PAYMENT_CHOICE =[('ON', 'Online payment'), ('COD', "Cash On delivery")]
    fruit_name = models.CharField(max_length=10)
    fruit_quan = models.IntegerField()
    delivery_address = models.CharField(max_length=20)
    delivery_date = models.DateField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICE)
