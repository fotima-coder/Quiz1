from django.contrib.auth.models import AbstractUser
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    class ROLE(models.TextChoices):
        ADMIN ='ADMIN','Admin'
        TEACHER ='Teacher','Teacher'
        STUDENT = 'Student','Student'

    role = models.CharField(max_length=10, choices=ROLE.choices, default=ROLE.ADMIN)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}({self.role})"