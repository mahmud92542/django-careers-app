from django.shortcuts import render

def index(request):
	return render (request,"index.html")

def joblisting(request):
	return render (request,"job-listings.html")

def aboutme(request):
	return render (request,"about.html")
