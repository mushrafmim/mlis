# Generated by Django 5.0.6 on 2024-05-27 03:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportgenapp', '0002_rename_specimentype_reportformats_specimen_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportgen',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportgen',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
