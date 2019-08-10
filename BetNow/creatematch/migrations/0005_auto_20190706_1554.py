# Generated by Django 2.1.7 on 2019-07-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatematch', '0004_auto_20190706_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='category',
            field=models.CharField(choices=[('cricket', 'Cricket'), ('kabbadi', 'Kabbadi'), ('football', 'FootBall')], default='Cricket', max_length=10),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
