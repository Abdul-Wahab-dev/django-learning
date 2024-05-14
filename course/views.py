from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    learning = {"name":"django"}
    return render(request , "course1.html",context=learning)

def test(request):
    return HttpResponse("OK")