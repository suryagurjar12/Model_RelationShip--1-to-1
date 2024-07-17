from django.db import models

# Create your models here.
class Adhar(models.Model):
    adhar_no=models.IntegerField(unique=True)
    create_date=models.DateTimeField()
    create_by=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.adhar_no)
    
    
    
class Student(models.Model):
    Name=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Email=models.EmailField()
    adhar_no=models.OneToOneField(Adhar,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name
        
