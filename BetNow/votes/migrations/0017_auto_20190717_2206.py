# Generated by Django 2.1.7 on 2019-07-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0016_auto_20190717_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservotes',
            name='team',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uservotes',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
