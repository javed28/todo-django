from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=20,null=True)
    emp_name = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.emp_name
    