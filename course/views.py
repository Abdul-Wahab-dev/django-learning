from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import CourseRegistration
from django.contrib import messages
from django.views.decorators.cache import cache_page
# Create your views here.



def index(request):
    if request.method == "POST":
        form = CourseRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            desc = form.cleaned_data['description']
            print(name , desc)
            form.save(True)
            # form.save(name=name , description=desc)
            # reg = Course(id=1,name=name,description=desc)
            # reg.save()
            messages.add_message(request,messages.SUCCESS,"you have sucessfully registered!")
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

@cache_page(60)
def showCourse(request , my_id , **check):
    print(my_id)
    print(check)
    
    return render(request, 'course1.html' , context={"name":my_id})