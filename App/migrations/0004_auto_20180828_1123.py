# Generated by Django 2.1 on 2018-08-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20180828_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
