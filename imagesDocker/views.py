from django.shortcuts import render, HttpResponse


def home(request):
	return render(request, "imagesDockerForm.html", {'teste':'Eric M Carvalho','images':'images'})
