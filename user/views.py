from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth import authenticate
def homepage(request):
    return render(request,"homepage.html")

def registration(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"account was created for " + user )
            return redirect('login')
        
    context = {'form':form}
    return render(request,"registration.html",context)


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