# Generated by Django 5.0.4 on 2024-04-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0002_rename_user_id_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]