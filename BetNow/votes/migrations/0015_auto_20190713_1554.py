# Generated by Django 2.1.7 on 2019-07-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0014_uservotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservotes',
            name='is_voted',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
