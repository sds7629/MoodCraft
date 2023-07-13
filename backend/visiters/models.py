from django.db import models

class Visiter(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    
    class AgeChoice(models.TextChoices):
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
      