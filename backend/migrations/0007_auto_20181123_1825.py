# Generated by Django 2.1.3 on 2018-11-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20181123_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_details',
            name='userid',
            field=models.CharField(max_length=10),
        ),
    ]
