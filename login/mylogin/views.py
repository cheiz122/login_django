
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login as login1
from .forms import loginform,addrecordform
from .models import name
from django.template import loader
# Create your views here.

def login(request):
    return render(request,'login.html')


def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user.is_authenticated:
            messages.success(request,f"login succesful,Welcome :{username}")
            users=name.objects.all().values()
            template=loader.get_template('home.html')
            context={
            'users':users
                        }
            return HttpResponse(template.render(context,request))
        else:
            return render(request,"login.html") 
        
def page(request):
    
    return render(request,'register.html')
    
def register(request):
	if request.method == 'POST':
		form = loginform(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
            #user1=User(username=username,password=password)
			login1(request, user)
			messages.success(request, f"You Have Successfully Registered! Welcome!")
			return render(request,'login.html')
	else:
		form = loginform()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
def home1(request):
      users=name.objects.all().values()
      template=loader.get_template('home.html')
      context={
            'users':users
     }
      return HttpResponse(template.render(context,request))
def add_name(request):
    form=addrecordform(request.POST or None)
    if request.method == 'POST':
          if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
    return render(request, 'register_user.html', {'form':form})
         
		
	
    

       




    
 