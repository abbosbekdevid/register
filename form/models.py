from django.db import models

# Create your models here.


class PersonModel(models.Model):
    full_name  = models.CharField(max_length=80)
    user_name  = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    number = models.IntegerField(default = 18)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.full_name