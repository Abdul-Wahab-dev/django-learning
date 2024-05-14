from django.shortcuts import render
from django.http import HttpResponse


def fees_index(request):
    fees={'fee':20000}
    return render(request , "fee1.html",context=fees)
# Create your views here.
