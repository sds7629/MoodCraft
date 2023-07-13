from django.db import models
from django.db.models import Count
# Create your models here.
class Result(models.Model):
    drink_kind = models.CharField(max_length = 50)
    drink_count = models.PositiveIntegerField(default = 0, blank=True, verbose_name= "총 결과 값")
    description = models.TextField()

    def __str__(self):
        return self.drink_kind