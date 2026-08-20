from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        DEAN = "dean", "Dean"
        STUDENT = "student", "Student"
        MENTOR = "mentor", "Mentor"
        HOD = "hod", "HOD"

    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
    )

    def __str__(self):
        return self.username