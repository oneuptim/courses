from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
	context = {'name': Course.objects.all()
	}
	return render(request, 'add_des/index.html', context)

def process(request):
		if request.method == 'POST':
			Course.objects.create(name=request.POST['name'], description=request.POST['description'])
			return redirect('/')

def remove(request, id):
	print id

	course = Course.objects.filter(id=id)
	
	print course
	context = {
		'id': id,
		'course': course[0],
	}
	return render(request, 'add_des/remove.html',context)

def destroy(request, id):
	
	Course.objects.filter(id=id).delete()
	return redirect('/')
		
	