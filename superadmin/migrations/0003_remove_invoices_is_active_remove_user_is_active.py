# Generated by Django 5.0.2 on 2024-02-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_invoices_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
