# Generated by Django 3.2.19 on 2023-07-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesorders', '0010_auto_20230719_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Item Name'),
        ),
    ]