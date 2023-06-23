from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ManagerDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    corpid = models.CharField(max_length=50,null=True)
    department = models.CharField(max_length=50,null=True)
    # designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)
    
    def __str__(self):
        return self.user.username
    
class EmployeeData(models.Model):
    fullname = models.CharField(max_length=200)
    emp_id = models.IntegerField()
    emailid = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    department = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)
    
    
