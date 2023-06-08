from django.db import models

# Create your models here.

# Company Model

class Company(models.Model):
    object=None
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones')))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


#Employee Model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=11)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','SD'),
        ('Project Lead','PL')
    ))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)
