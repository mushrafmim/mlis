# Generated by Django 5.0.6 on 2024-05-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportgenapp', '0011_alter_reportrequest_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportrequest',
            name='age',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportrequest',
            name='gender',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportrequest',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]