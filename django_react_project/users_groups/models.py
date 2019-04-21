from django.db import models


class User(models.Model):
    username = models.CharField('username', max_length=255)
    created = models.DateTimeField('Created at', auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE,)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField('name', max_length=255, null=False, blank=False)
    description = models.CharField('description', null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name
