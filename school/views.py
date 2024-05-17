from django.shortcuts import render
from .models import Student,ExamCenter
# Create your views here.


def students(request):
    print('working')
    data = Student.customStu.all()
    return render(request , 'school/home.html' , {'data':data})
