# Generated by Django 3.2.20 on 2023-12-16 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0012_alter_meetup_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('DevRel', 'DevRel'), ('DevOps', 'DevOps')], default='DevRel', max_length=10, verbose_name='Область навыков'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(choices=[('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Улан-Удэ', 'Улан-Удэ'), ('Казань', 'Казань')], default='Москва', max_length=15, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='user',
            name='master',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Junior', max_length=6, verbose_name='Навык'),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 18, 9, 36, 521125, tzinfo=utc), verbose_name='Дата начала'),
        ),
    ]
