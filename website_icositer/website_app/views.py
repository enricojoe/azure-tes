from django.shortcuts import render

# Create your views here.
def homepage (request):
	return render(request,'home/home.html')

def about (request):
	return render(request,'about/about.html')

def competition (request):
	return render(request,'competition/competition.html')

def conference (request):
	return render(request,'conference/conference.html')