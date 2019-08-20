from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import File
import os, shutil
from os.path import join

def TrainView(request):
	template_name = 'tula/train.html'
	return render(request, 'tula/train.html')

def TopFrameView(request):
	template_name = 'tula/topframe.html'
	return render(request, 'tula/topframe.html')

def BottomFrameView(request):
	template_name = 'tula/bottomframe.html'
	return render(request, 'tula/bottomframe.html')

def RealTimeView(request):
	template_name = 'tula/real_time_view.html'
	return render(request, 'tula/real_time_view.html')

def HomeView(request):
	template_name = 'tula/home.html'
	return render(request, 'tula/home.html')

def list_choice(request):

	File.objects.all().delete()
	selected_choice = request.POST['status']

	if selected_choice == 'accepted':
		return HttpResponseRedirect('/tula/accepted_list/')
	elif selected_choice == 'rejected': 		
		return HttpResponseRedirect('/tula/rejected_list/')


def accepted_list(request):
	#File.objects.all().delete()
	#for files in os.listdir('C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\accepted'):
	for files in os.listdir('media/images/accepted'):
			f = File.objects.filter(file_name = files,status='accepted')
			if len(f) > 0:
				continue
				#print('Imagem já existe')
			else:
				if "chart" not in files:
					File.create(files,'accepted')
				#print('Imagem não existe!')
	files = File.objects.filter(status='accepted')
	return render(request, 'tula/results.html', {'files': files})

def rejected_list(request):
	#for files in os.listdir('C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\rejected'):
	for files in os.listdir('media/images/rejected'):
			f = File.objects.filter(file_name = files,status='rejected')

			if len(f) > 0:
				continue
				#print('Imagem já existe')
			else:
				if "chart" not in files:
					File.create(files,'rejected')
				#print('Imagem não existe!')
	files = File.objects.filter(status='rejected')
	return render(request, 'tula/results_rejected.html', {'files': files})	


def recent(request):
	string = "python image_get.py"
	os.system(string)
	files = os.listdir('media/images/recent')
	if files[0][9] == '1':
		file_status = 'Rejected'
	else:
		file_status = 'Accepted'
	return render(request, 'tula/bottomframe.html', {'file': files[0] , 'file_status':file_status})	

def editview(request,file_name):
	print(file_name)
	return render(request, 'tula/edit.html', {'file_name': file_name})

def editview_rejected(request,file_name):
	print(file_name)
	return render(request, 'tula/edit_rejected.html', {'file_name': file_name})


def switch(request,file_name):
	f = File.objects.filter(file_name=file_name)
	#print(f)
	f.update(status='rejected')
	#shutil.move('C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\accepted\\'+file_name,'C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\rejected\\')
	string = "python imgclassifier0.1.py media/images/accepted/" + file_name +" 1"
	print('Executed "',string, '"to REJECT image')
	os.system(string)
	#print(file_name)
	return HttpResponseRedirect('/tula/accepted_list/')


def switch_rejected(request,file_name):
	f = File.objects.filter(file_name=file_name)
	#print(f)
	f.update(status='accepted')
	#shutil.move('C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\rejected\\'+file_name,'C:\\Users\\Roberto.Oliveira\\Desktop\\sapec_interface\\mysite\\media\\images\\accepted\\')
	string = "python imgclassifier0.1.py media/images/rejected/" + file_name +" 0"
	print('Executed "',string, '"to ACCEPT image')
	os.system(string)
	#print(file_name)
	return HttpResponseRedirect('/tula/rejected_list/')


