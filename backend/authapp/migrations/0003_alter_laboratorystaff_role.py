# Generated by Django 5.0.6 on 2024-05-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_rename_staff_address_laboratorystaff_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorystaff',
            name='role',
            field=models.CharField(default='Laboratory Staff', max_length=50),
        ),
    ]