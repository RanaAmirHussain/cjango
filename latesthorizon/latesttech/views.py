from django.shortcuts import render
from.forms import Imageform
from .models import Image
from . import views

# Create your views here.



def home(request):


    if request.method == "POST":
       form = Imageform(request.POST , request.FILES)
       if form.is_valid():
           form.save()
           form = Imageform()
           img = Image.objects.all    
    return render(request,"home1.html",{'img':img,'form':form} )
