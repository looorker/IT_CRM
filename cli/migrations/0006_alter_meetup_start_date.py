# Generated by Django 3.2.20 on 2023-12-15 23:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0005_alter_meetup_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 15, 23, 42, 19, 166579, tzinfo=utc), verbose_name='Дата начала'),
        ),
    ]
