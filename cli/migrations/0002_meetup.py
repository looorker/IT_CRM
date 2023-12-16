# Generated by Django 3.2.20 on 2023-12-15 16:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('area', models.CharField(max_length=100, verbose_name='Сфера')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('start_date', models.DateField(default=datetime.datetime(2023, 12, 15, 16, 33, 39, 34759, tzinfo=utc), verbose_name='Дата начала')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cli.user')),
            ],
        ),
    ]