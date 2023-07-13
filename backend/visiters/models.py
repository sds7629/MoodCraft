from django.db import models

class Visiter(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    gender = models.CharField(max_length=10, choices=GenderChoice.choices, null=True)
    age = models.PositiveIntegerField(default=0)    
 
    def __str__(self):
        return self.gender, self.age
    
# class Count(models.Model):
    
#     count = models.PositiveIntegerField(default=0)

#     @property
#     def click(self):
#         self.count += 1
#         self.save()
#         return self.count