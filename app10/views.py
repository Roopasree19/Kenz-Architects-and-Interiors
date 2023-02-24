from django.shortcuts import render
from app10.models import *
from django.http import HttpResponseRedirect

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
	if request.session.has_key("my_id"):
		return render(request,'admin/index.html')
	else:
		return HttpResponseRedirect('/admin_login')

		
def admin_register(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		cpass=request.POST['confirmpassword']
		check=reg_tb.objects.filter(email=cemail)
		if check:
			return render(request,'admin/register.html',{'error':'Already registered'})
		else:
			add=reg_tb(email=cemail,password=cpassword,conformpassword=cpass)
			add.save()
		return render(request,'admin/index.html',{'success':"successfully registered"})
	else:
	    return render(request,'admin/register.html')

def admin_login(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		check=reg_tb.objects.filter(email=cemail,password=cpassword)
		if check:
			for x in check:
				request.session['id']=x.id
				request.session['email']=x.email
			return render(request,'admin/index.html',{'success':'successfully logined'})
		else:
			return render(request,'admin/login.html',{'error':' invalid details'})
	else:
		return render(request,'admin/login.html')


def admin_logout(request):
	if request.session.has_key("id"):
	    del request.session['id']
	    del request.session['email']
	return HttpResponseRedirect ('/admin_login/')
