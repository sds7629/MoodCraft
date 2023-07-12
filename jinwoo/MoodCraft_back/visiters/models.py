from django.db import models

class Visiter(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    gender = models.CharField(max_length=10, choices=GenderChoice.choices)
    age = models.PositiveIntegerField(default=0)