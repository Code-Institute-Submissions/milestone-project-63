# Generated by Django 3.0.6 on 2020-05-15 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200513_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subscription_plan',
        ),
    ]
