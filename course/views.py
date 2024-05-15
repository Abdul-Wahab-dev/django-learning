from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from course.models import Course
from .form import CourseRegistration
from .models import Course
# Create your views here.



def index(request):
    if request.method == "POST":
        form = CourseRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            desc = form.cleaned_data['description']
            form.save(name=name , description=desc)
            # reg = Course(id=1,name=name,description=desc)
            # reg.save()
            # return HttpResponseRedirect('/course/success')
        print("coming from POST request")
    else:
        form = CourseRegistration()
        print("Coming from GET request")
    
    return render(request , "course1.html",context={"form":form})

def test(request):
    return HttpResponse("OK")

def success(request):
    return render(request, 'success.html')