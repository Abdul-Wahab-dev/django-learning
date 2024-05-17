from django.contrib import admin
from .models import Student, Teacher , Contractor , ExamCenter , MyExamCenterProxy , Pages




# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
    
@admin.register(Contractor)
class ContracterAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
    
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']    
    
@admin.register(MyExamCenterProxy)
class ExamCenterProxyAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']    
    
    
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat','publish','student']    