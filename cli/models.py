from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=20, blank=False)
    sername = models.CharField('Фамилия', max_length=20, blank=False)
    age = models.PositiveIntegerField('Возраст', blank=False)
    description = models.TextField('Немного о себе', max_length=500, blank=True)
    email = models.EmailField('Почта', blank=False)

    def __str__(self):
        return f'{self.name} {self.sername}'
