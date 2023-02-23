from django.shortcuts import render
from app10.models import *

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')

def gallery(request):
	return render(request,'gallery.html')

def projects(request):
	return render(request,'projects.html')

def services(request):
	return render(request,'services.html')






#############################################################################
def admin_index(request):
	return render(request,'admin/index.html')

def admin_register(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		cpass=request.POST['confirmpassword']
		check=reg_tb.objects.filter(email=cemail)
		if check:
			return render(request,'admin/register.html',{'error':'already registered'})
		else:
			add=reg_tb(email=cemail,password=cpassword,conformpassword=cpass)
			add.save()
		return render(request,'admin/index.html',{'success':"data saved"})
	else:
	    return render(request,'admin/register.html')

def admin_login(request):
	return render(request,'admin/login.html')