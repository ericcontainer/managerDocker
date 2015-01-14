from django.shortcuts import render, HttpResponse


def add_repo(request):
	return render(request, "imagesDockerForm.html")
