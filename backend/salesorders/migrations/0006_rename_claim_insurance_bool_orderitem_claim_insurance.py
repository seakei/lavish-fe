# Generated by Django 3.2.19 on 2023-06-28 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesorders', '0005_auto_20230627_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='claim_insurance_bool',
            new_name='claim_insurance',
        ),
    ]