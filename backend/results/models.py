from django.db import models

# Create your models here.
class Result(models.Model):
    drink_kind = models.CharField(max_length = 50)
    drink_count = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()