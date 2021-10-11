from django.db import models

class Creator(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.first_name
    
class Languages(models.Model):
    name=models.CharField(max_length=50)
    creator=models.OneToOneField(Creator,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class Frameworks(models.Model):
    name=models.CharField(max_length=50)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    
class Programer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    language=models.ManyToManyField(Languages)
    
    def __str__(self) -> str:
        return self.first_name