# Generated by Django 2.1.7 on 2019-07-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatematch', '0011_auto_20190709_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='col_amt',
            field=models.IntegerField(default=0),
        ),
    ]