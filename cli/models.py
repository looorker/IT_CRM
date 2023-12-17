from django.utils import timezone

from django.db import models

mastery = {'Junior': 'Junior', 'Middle': 'Middle', 'Senior': 'Senior'}
area = {'Frontend': 'Frontend', 'Backend': 'Backend', 'DevRel': 'DevRel', 'DevOps': 'DevOps'}
city = {'Москва': 'Москва', 'Санкт-Петербург': 'Санкт-Петербург', 'Улан-Удэ': 'Улан-Удэ', 'Казань': 'Казань'}


class User(models.Model):
    name = models.CharField('Имя', max_length=20, blank=False)
    sername = models.CharField('Фамилия', max_length=20, blank=False)
    age = models.PositiveIntegerField('Возраст', blank=False)
    description = models.TextField('Немного о себе', max_length=500, blank=True)
    master = models.CharField('Навык', choices=mastery.items(), max_length=6, default='Junior')
    area = models.CharField('Область навыков', choices=area.items(), max_length=10, default='DevRel')
    city = models.CharField('Город', choices=city.items(), max_length=15, default='Москва')
    email = models.EmailField('Почта', blank=False)

    def __str__(self):
        return f'{self.name} {self.sername}'


class Meetup(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField('Название', max_length=100, blank=False)
    area = models.CharField('Сфера', max_length=100, blank=False)
    description = models.TextField('Описание', max_length=500, blank=True)
    start_date = models.DateField('Дата начала', blank=False, default=timezone.now)

    def get_absolute_url(self):
        return f'cli/{self.id}'

    def get_users(self) -> int:
        return self.user.count()

    def __str__(self):
        return f'{self.name}'
