# Generated by Django 2.1.7 on 2019-07-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
