# Generated by Django 2.0.4 on 2018-05-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20180501_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
