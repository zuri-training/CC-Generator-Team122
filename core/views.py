from django.shortcuts import render
from django.views import generic
import mimetypes
from django.http import HttpResponse
import os
from zipfile import ZipFile
import zipfile
class home(generic.TemplateView) :
    template_name = "landingpage.html"
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
class index(generic.TemplateView) :
    template_name = "index.html"



def download_flower1(request, filename=''):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = ZipFile('Flower1.zip')
        file_path = BASE_DIR + '/static/cardfiles/' + filename
        path = open(file_path, "r")
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
    else:
        return render(request, 'Flower1.zip')
    return response