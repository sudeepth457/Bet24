# Generated by Django 2.1.7 on 2019-07-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatematch', '0005_auto_20190706_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]