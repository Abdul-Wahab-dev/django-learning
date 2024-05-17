from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    class Meta:
        abstract = True

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    
class MyExamCenterProxy(ExamCenter):
    class Meta:
        proxy = True    
        ordering = ['id']

# Custom manager
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

# Create your models here.
class Student(CommonInfo, ExamCenter):
    fees = models.IntegerField()
    students = models.Manager()
    customStu = CustomManager()
    
    
class Pages(models.Model):
        student = models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True)
        page_name = models.CharField(max_length=70)
        page_cat = models.CharField(max_length=70)
        publish = models.DateField()
        
        
class Teacher(CommonInfo):
    salary = models.IntegerField()
    
class Contractor(CommonInfo):
    payment = models.IntegerField()
    
    
