# Generated by Django 2.1.7 on 2019-07-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0015_auto_20190713_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservotes',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uservotes',
            name='mnumber',
            field=models.CharField(max_length=20),
        ),
    ]