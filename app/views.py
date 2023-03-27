from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
def fbv_string(request):
    return HttpResponse('<h1>This fbv string</h1>')
#returning string by using cbv
class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>cbv string</h1>')
def fbv_html(request):
    d={'name':"lokitha"}
    return render(request,'fbv_html.html',d)
#returning html and sending context by cbv
class cbv_html(View):
    def get(self,request):
        d={'form':"saritha"}
        return render(request,'cbv_html.html',d)
def fbv_djform(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'fbv_djform.html',d)
#Dealing with Django form by using CBV
class cbv_djform(View):
    def get(self,request):
        NF=NameForm()
        d={'form':NF}
        return render(request,'cbv_djform.html',d)

def fbv_mdform(request):
    SF=StudentForm()
    d={'form':SF}
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Inserted Data')
    return render(request,'fbv_mdform.html',d)

# Dealing with Model forms by CBV
class cbv_mdform(View):
    def get(self,request):
        SF=StudentForm()
        d={'form':SF}
        return render(request,'cbv_mdform.html',d)

    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Inserted Data')


class cbv_tvhtml(TemplateView):
    template_name='cbv_html.html'


