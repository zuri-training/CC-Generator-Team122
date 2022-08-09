from django.shortcuts import render
from django.views import generic


class home(generic.TemplateView) :
    template_name = "home.html"
class about_us(generic.TemplateView) :
    template_name = "about_us.html"