from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, "base/home.html")


@login_required
def base_files(request, filename):
    location = "base/" + filename
    return render(request, location, {}, content_type="text/plain")
