from django.shortcuts import render
from app10.models import *
from django.http import HttpResponseRedirect
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
	data=project_tb.objects.all()
	return render(request,'index.html',{'data':data})

def about(request):
	return render(request,'about.html')


def contact(request):
	if request.method == "POST":
		cname=request.POST['name']
		cemail=request.POST['email']
		cphone=request.POST['phone']
		csubject=request.POST['subject']
		cmessage=request.POST['message']
		check=contact_tb.objects.filter(email=cemail)
		if check:
			return render(request,'contact.html',{'error':'already registered'})
		else:
			add=contact_tb(name=cname,email=cemail,phone=cphone,subject=csubject,message=cmessage)
			add.save()

			x = ''.join(random.choices(cname + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'welcome to Kenz Architects and Interiors'
			message = f'Hi {cname}, thank you for visiting Kenz Architects and Interiors'
			email_from = settings.EMAIL_HOST_USER 
			recipient_list = [cemail, ] 
			send_mail( subject, message, email_from, recipient_list ) 

			return render(request,'index.html',{'success':"data saved"})
	else:
		return render(request,'contact.html')

def contactus(request):
	if request.method == "POST":
		cname=request.POST['name']
		cemail=request.POST['email']
		cphone=request.POST['phone']
		csubject=request.POST['subject']
		cmessage=request.POST['message']
		check=contact_tb.objects.filter(email=cemail)
		if check:
			return render(request,'index.html',{'error':'already registered'})
		else:
			add=contact_tb(name=cname,email=cemail,phone=cphone,subject=csubject,message=cmessage)
			add.save()

			return render(request,'index.html',{'success':"data saved"})
	else:
		return render(request,'contact.html')


	

def get(request):
	if request.method == "POST":
		cname=request.POST['name']
		cphone=request.POST['phone']
		cmessage=request.POST['message']
		check=getin_tb.objects.filter(phone=cphone)
		if check:
			return render(request,'get.html',{'error':'already registered'})
		else:
			add=getin_tb(name=cname,phone=cphone,message=cmessage)
			add.save()

			return render(request,'index.html',{'success':"data saved"})
	else:
		return render(request,'get.html')

	

def gallery(request):
	data=gallery_tb.objects.all()
	return render(request,'gallery.html',{'data':data})

def projects(request):
	data=project_tb.objects.all()
	return render(request,'projects.html',{'details':data})

def services(request):
	data=service_tb.objects.all()
	return render(request,'services.html',{'details':data})

def servicespage(request):
	fid=request.GET['uid']
	data=service_tb.objects.filter(id=fid)
	return render(request,'servicespage.html',{'details':data})








#############################################################################
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



def  admin_service(request):
	if request.method == "POST":
		cname=request.POST['name']
		cdesc=request.POST['desc']
		cimage=request.FILES['image']
		check=service_tb.objects.filter(name=cname)
		if check:
			return render(request,'admin/service.html',{'error':'already registered'})
		else:
			add=service_tb(name=cname,desc=cdesc,image=cimage)
			add.save()
		return render(request,'admin/index.html',{'success':"data saved"})
	else:
		return render(request,'admin/service.html')


def admin_servtb(request):
	data=service_tb.objects.all()
	return render(request,'admin/servtb.html',{'details':data})

def admin_servupd(request):
	if request.method == "POST":
		cname=request.POST['name']
		cdesc=request.POST['desc']
		fid=request.GET['uid']
		imgval=request.POST['imgup']
		if imgval =="yes":

			cimage=request.FILES['image']
			oldrec=service_tb.objects.filter(id=fid)
			updrec=service_tb.objects.get(id=fid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('successfully deleted')
			updrec.image=cimage
			updrec.save()

        
		add=service_tb.objects.filter(id=fid).update(name=cname,desc=cdesc)
		return HttpResponseRedirect('/admin_servtb/')
	else:
		fid=request.GET['uid']
		data=service_tb.objects.filter(id=fid)
		return render(request,"admin/servupd.html",{'details':data})

def admin_servdlt(request):
	    fid=request.GET['did']
	    oldrec=service_tb.objects.filter(id=fid)
	    for x in oldrec:
	    	imgurl=x.image.url
	    	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
	    	if os.path.exists(pathtoimage):
	    		os.remove(pathtoimage)
	    data=service_tb.objects.filter(id=fid).delete()
	    return HttpResponseRedirect('/admin_servtb/')


def  admin_projects(request):
	if request.method == "POST":
		cname=request.POST['name']
		cimage=request.FILES['image']
		check=project_tb.objects.filter(name=cname)
		if check:
			return render(request,'admin/projects.html',{'error':'already registered'})
		else:
			add=project_tb(name=cname,image=cimage)
			add.save()
		return render(request,'admin/index.html',{'success':"data saved"})
	else:
		return render(request,'admin/projects.html')


def admin_protb(request):
	data=project_tb.objects.all()
	return render(request,'admin/protb.html',{'details':data})



def admin_projupd(request):
	if request.method == "POST":
		cname=request.POST['name']
		fid=request.GET['uid']
		imgval=request.POST['imgup']
		if imgval =="yes":

			cimage=request.FILES['image']
			oldrec=project_tb.objects.filter(id=fid)
			updrec=project_tb.objects.get(id=fid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('successfully deleted')
			updrec.image=cimage
			updrec.save()

        
		add=project_tb.objects.filter(id=fid).update(name=cname)
		return HttpResponseRedirect('/admin_protb/')

	else:
		fid=request.GET['uid']
		data=project_tb.objects.filter(id=fid)
		return render(request,"admin/projupd.html",{'details':data})


def admin_projdlt(request):
	    fid=request.GET['did']
	    oldrec=project_tb.objects.filter(id=fid)
	    for x in oldrec:
	    	imgurl=x.image.url
	    	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
	    	if os.path.exists(pathtoimage):
	    		os.remove(pathtoimage)
	    data=project_tb.objects.filter(id=fid).delete()
	    return HttpResponseRedirect('/admin_protb/')


def  admin_gallery(request):
	if request.method == "POST":
		cimage=request.FILES['image']
		check=gallery_tb.objects.filter(image=cimage)
		if check:
			return render(request,'admin/gallery.html',{'error':'already registered'})
		else:
			add=gallery_tb(image=cimage)
			add.save()
		return render(request,'admin/index.html',{'success':"data saved"})
	else:
		return render(request,'admin/gallery.html')

def admin_gallerytb(request):
	data=gallery_tb.objects.all()
	return render(request,'admin/gallerytb.html',{'details':data})



def admin_galldlt(request):
	    fid=request.GET['did']
	    oldrec=gallery_tb.objects.filter(id=fid)
	    for x in oldrec:
	    	imgurl=x.image.url
	    	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
	    	if os.path.exists(pathtoimage):
	    		os.remove(pathtoimage)
	    data=gallery_tb.objects.filter(id=fid).delete()
	    return HttpResponseRedirect('/admin_gallerytb/')





def admin_contacttb(request):
	data=contact_tb.objects.all()
	return render(request,'admin/contacttb.html',{'details':data})

def admin_usertb(request):
	data=getin_tb.objects.all()
	return render(request,'admin/usertb.html',{'details':data})



