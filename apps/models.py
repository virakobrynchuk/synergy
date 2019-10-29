from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('groups_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('groups_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('groups_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('users_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('users_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('users_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username
