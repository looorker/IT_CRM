# Generated by Django 3.2.20 on 2023-12-16 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0013_auto_20231216_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала'),
        ),
    ]
