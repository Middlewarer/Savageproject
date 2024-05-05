from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/index.html'

class NotHomeView(TemplateView):
    template_name = 'main/not_home.html'
