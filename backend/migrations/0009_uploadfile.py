# Generated by Django 2.1.3 on 2019-04-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20181123_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='uploaded file')),
            ],
        ),
    ]
