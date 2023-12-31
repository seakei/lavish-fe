# Generated by Django 3.2.19 on 2023-07-09 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salesorders', '0008_auto_20230704_2237'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Required, PrimaryKey none-editable', primary_key=True, serialize=False, verbose_name='UUID Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this data is active or deleted', verbose_name='Active')),
                ('condition', models.BooleanField(blank=True, default=False, null=True, verbose_name='Condition')),
                ('remarks', models.CharField(blank=True, max_length=255, null=True, verbose_name='Remarks')),
                ('signature_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='SignatureId')),
                ('number', models.CharField(blank=True, default='', max_length=25, verbose_name='Number')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspection_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('order_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='salesorders.orderitem', verbose_name='Order_item')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspection_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Inspection',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='InspectionSignature',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Required, PrimaryKey none-editable', primary_key=True, serialize=False, verbose_name='UUID Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this data is active or deleted', verbose_name='Active')),
                ('signature_data', models.BinaryField(blank=True, null=True, verbose_name='Signature Image Data')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspectionsignature_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspection_sig', to='inspections.inspection')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspectionsignature_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Inspection Signature',
            },
        ),
        migrations.CreateModel(
            name='InspectionPicture',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Required, PrimaryKey none-editable', primary_key=True, serialize=False, verbose_name='UUID Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this data is active or deleted', verbose_name='Active')),
                ('image_data', models.FileField(blank=True, null=True, upload_to='', verbose_name='Inspection Pic File')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspectionpicture_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspection', to='inspections.inspection')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections_inspectionpicture_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Inspection Picture',
            },
        ),
    ]
