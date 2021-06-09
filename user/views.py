from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
def homepage(request):
    return render(request,"homepage.html")

def login(request):
    
    if request.method  == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username , password=password)
        
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'username or password is wrong')
            
    context = {}
    return render(request,"login.html",context)