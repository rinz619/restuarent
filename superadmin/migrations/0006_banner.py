# Generated by Django 5.0.4 on 2024-04-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0005_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=1)),
                ('image', models.FileField(blank=True, null=True, upload_to='banner')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
