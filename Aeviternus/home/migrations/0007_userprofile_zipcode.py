# Generated by Django 2.0.4 on 2018-04-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180429_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Zipcode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
