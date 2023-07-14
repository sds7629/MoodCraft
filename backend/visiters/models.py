from django.db import models
from results.models import Result,ResultDetailModel

class Visiter(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    
    class AgeChoice(models.TextChoices):
<<<<<<< HEAD
        TWENTY = ("twenty","20대")
        THIRTY = ("thirty","30대")
        FORTY = ("forty", "40대")
        FIFTY = ("fifty","50대")

    gender = models.CharField(max_length=10, choices=GenderChoice.choices, null=True)
    age = models.CharField(max_length=10,choices=AgeChoice.choices, null=True )    
    result = models.ForeignKey("results.Result",on_delete=models.CASCADE, null=True)
    result_detail = models.ForeignKey("results.ResultDetailModel", on_delete= models.CASCADE, null=True)
    
    
=======
        TWENTY = ("Twenty","20대")
        THIRTY = ("Thirty","30대")
        FORTY = ("Forty", "40대")
        FIFTY = ("Fifty","50대")

    gender = models.CharField(max_length=10, choices=GenderChoice.choices, null=True)
    age = models.CharField(max_length=10,choices=AgeChoice.choices, null=True )    
   
# class Count(models.Model):
    
#     count = models.PositiveIntegerField(default=0)

#     @property
#     def update_counter(self):
#         self.count += 1
#         self.save()
      
>>>>>>> 0f72ee030948cd426dd102df9338d0d358bffc5c
