# Generated by Django 3.2.20 on 2023-12-16 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0008_alter_meetup_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 11, 29, 7, 602768, tzinfo=utc), verbose_name='Дата начала'),
        ),
    ]
