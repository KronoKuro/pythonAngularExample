from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

class Employees(models.Model):
    Id = models.AutoField(primary_key=True)
    EmployeName = models.CharField(max_length=200)
    Department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    DateJoin = models.CharField(max_length=200)
    PhotoFileName = models.CharField(max_length=200)
