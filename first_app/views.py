from django.shortcuts import render
from . import forms

from django.http import HttpResponse

# Create your views here.
from first_app.models import Topic,Webpage,AccessRecord

#variable
#my_dict=[]


#functions
def index(request):
    web_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_rec':web_list}
    return render(request,'first_app/index.html',context = my_dict)
    #return my_dict

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
            #return render(request, 'first_app/index.html',context=index(request))

            #built in validator



    return render(request, 'first_app/form.html',{'form':form})