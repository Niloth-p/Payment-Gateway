# Generated by Django 3.0.8 on 2020-07-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razorpayapp', '0002_auto_20200730_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razorpayhistory',
            name='authcode',
            field=models.IntegerField(null=True),
        ),
    ]
