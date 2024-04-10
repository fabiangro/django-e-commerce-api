from django.db import models


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.CASCADE)
    product = models.ForeignKey('Products', models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_items'
        unique_together = (('order', 'product'),)


class Orders(models.Model):
    user = models.ForeignKey('Users', models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    image = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    nick = models.CharField(max_length=16)
    email = models.CharField(max_length=30)
    password = models.CharField()
    admin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
