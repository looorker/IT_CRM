# Generated by Django 3.2.20 on 2023-12-15 20:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0003_auto_20231215_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 15, 20, 32, 53, 245215, tzinfo=utc), verbose_name='Дата начала'),
        ),
    ]
