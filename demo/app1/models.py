from django.db import models

# Create your models here.




class CustomModel(models.Manager):
    def salary(self):
        return super(CustomModel,self).get_queryset().filter(esal__gt=5000)


class Employee(models.Model):
    ename = models.CharField(max_length=50)
    esal = models.FloatField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    objects = models.Manager()
    custom = CustomModel()




    def __str__(self):
        return f"{self.ename}--{self.esal}--{self.status}--{self.created}"


class Project(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)