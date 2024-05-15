from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course
# Create your views here.



def index(request):
    data = Course.objects.all()
    
    learning = {"name":"django"}
    
    return render(request , "course1.html",context={"data":data})

def test(request):
    return HttpResponse("OK")