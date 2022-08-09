from django.shortcuts import render
from django.views import generic


class home(generic.TemplateView) :
    template_name = "home.html"
class about_us(generic.TemplateView) :
    template_name = "about_us.html"
class contact_us(generic.TemplateView) :
    template_name = "contact_us.html"
class landingpage(generic.TemplateView) :
    template_name = "landingpage.html"
class library(generic.TemplateView) :
    template_name = "library.html"
class profile(generic.TemplateView) :
    template_name = "userprofile.html"
class documentation(generic.TemplateView) :
    template_name = "tutorials.html"
class api_ref(generic.TemplateView) :
    template_name = "apidoc.html"