# Generated by Django 2.2.1 on 2021-08-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boram_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='question10',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='reg_date',
            field=models.DateTimeField(),
        ),
    ]