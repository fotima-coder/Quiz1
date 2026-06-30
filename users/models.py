from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Group


class User(AbstractUser):
    class ROLE(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'

    role = models.CharField(
        max_length=10,
        choices=ROLE.choices,
        default=ROLE.STUDENT
    )

    student_groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='students'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"