from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    name ="emma"
    return render(request, "home/welcome.html", {"name": name})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, "home/authorized.html", {})