from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# convert function view to class view
# def home(request):
#     name ="emma"
#     return render(request, "home/welcome.html", {"today": datetime.today()})
class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, "home/authorized.html", {})

class Authorized(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = '/admin'

