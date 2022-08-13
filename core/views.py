from django.shortcuts import render
from django.views import generic
import mimetypes
from django.http import StreamingHttpResponse
import os
from zipfile import ZipFile
import zipfile
from wsgiref.util import FileWrapper


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



def download_flower1(request):
    filename = None
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = 'Flower1.zip'
        filepath = BASE_DIR + '/cardfiles/' + filename
        thefile = filepath
        filename = os.path.basename(thefile)
        chunk_size = 8192
        path = open(filepath, "r")
        response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),
            content_type=mimetypes.guess_type(thefile)[0])
        response['Content-Length'] = os.path.getsize(thefile)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        mime_type, _ = mimetypes.guess_type(filepath)
    else:
        return render(request, 'Flower1.zip')
    return response



def download_flower2(request):
    filename = None
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = 'Flower2.zip'
        filepath = BASE_DIR + '/cardfiles/' + filename
        thefile = filepath
        filename = os.path.basename(thefile)
        chunk_size = 8192
        path = open(filepath, "r")
        response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),
            content_type=mimetypes.guess_type(thefile)[0])
        response['Content-Length'] = os.path.getsize(thefile)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        mime_type, _ = mimetypes.guess_type(filepath)
    else:
        return render(request, 'Flower1.zip')
    return response