from django.shortcuts import render , HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , UserChangeForm
from django.contrib.auth import authenticate , login,logout
from .forms import SignupForm , EditUserProfileForm
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully !!')
    else:            
        fm = SignupForm()
    return render(request,'enroll/signup.html', {"form":fm})



def user_login(request):
   
    if request.method == 'POST':
        fm = AuthenticationForm(request=request , data=request.POST)
        print('login trigger')
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print(uname,upass)
            # fm.save()
            user = authenticate(request,username=uname, password=upass)
            print(user,'úser')
            if user is not None:
                login(request,user)
                messages.success(request,'You are loggedIn Successfully !!')
                return HttpResponseRedirect('/enroll/dashboard/')
    else:            
        fm = AuthenticationForm()
    return render(request,'enroll/login.html', {"form":fm})
   
   
    


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html' , {"name":request.user.username})
    else:
        return HttpResponseRedirect('/enroll/login/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')
        
        
def user_change_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user , data = request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/enroll/profile/")
    else:
        fm = PasswordChangeForm(user=request.user)        
    return render(request,'enroll/changepass.html' , {'form':fm})