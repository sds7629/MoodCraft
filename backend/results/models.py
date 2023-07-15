from django.db import models
from django.db.models import Count
# Create your models here.
class Result(models.Model):
    drink_kind = models.CharField(max_length = 50)
    name = models.CharField(max_length = 15, verbose_name="종류 이름")
    drink_count = models.PositiveIntegerField(default = 0, verbose_name= "총 결과 값")
    image = models.ImageField(blank = True, null = True, upload_to="uploads")
    description = models.TextField()

    def __str__(self):
        return self.drink_kind

class ResultDetailModel(models.Model):
    drink_name = models.CharField(max_length = 15, verbose_name= "술 이름 영어", blank = True, null = True)
    name = models.CharField(max_length = 15, verbose_name="술 이름", blank = True, null = True)
    description = models.TextField(verbose_name="설명", blank = True, null = True)
    dosu = models.CharField(max_length=10, verbose_name="도수")
    sweet = models.CharField(max_length= 20, verbose_name= "당도")
    image = models.ImageField(blank = True, null = True, upload_to="uploads")
    before_result = models.ForeignKey(
        "Result",
        related_name="results",
        on_delete= models.CASCADE,
        verbose_name="술 종류",
    )
    
    def __str__(self):
        return self.drink_name