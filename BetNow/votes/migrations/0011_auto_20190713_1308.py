# Generated by Django 2.1.7 on 2019-07-13 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0010_auto_20190713_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voterdetail',
            old_name='match',
            new_name='matchId',
        ),
    ]