# Generated by Django 3.0.5 on 2020-08-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_order_automobileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='endRent',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='startRent',
            field=models.DateField(null=True),
        ),
    ]
