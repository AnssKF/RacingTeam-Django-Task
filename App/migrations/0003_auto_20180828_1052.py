# Generated by Django 2.1 on 2018-08-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20180828_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(max_length=200),
        ),
    ]
