from django.http import HttpResponse
from email.policy import default
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
from sympy import stationary_points

from . import views
from django.shortcuts import render

from latesttech.models import School
from . import views


# def home(request):
#     return HttpResponse('chal par na yar mere')

def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def uploader(request):
    return render(request,'uploader.html')


def services(request):
     
    b=''
    if request.method == 'POST':
        name=request.POST.get('name')
        father_name=request.POST.get('father_name')
        gender=request.POST.get('gender')
        Class=request.POST.get('Class')
        section=request.POST.get('section')
        roll_no=request.POST.get('roll_no')                 
        data=School(name=name,father_name=father_name,gender=gender,Class=Class,section=section,roll_no=roll_no)
        data.save()
        b='your data has been sent sir you can go and check'
    return render(request,'contact.html',{'b':b})


   
def base(request):  
    # Atext=request.POST.get('text','default')
    # rpu=request.POST.get('rpu','off')
    # upper=request.POST.get('upper','off')
    # nl=request.POST.get('nl','off')  
    
    # if rpu == "on" :
        
    #     punctuations = ''' ? ` , : , @  ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] ,  ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
    #     analyzed=""
    #     for i in Atext:
    #         if i not in punctuations:
    #            analyzed=analyzed+i 
    #     data={'rpu': rpu , 'btext': analyzed }         
    #     return render(request,'base.html', data)
    # elif(upper == "on") :
    #     punctuations = '''?`,:,@;,%^<<,,,>>>{..!!!|“”,_-(),,[],,*,\\\}::"""'~,/,,#,$,&''' 
    #     analyzed=""
    #     for i in Atext:
    #         if i not in punctuations:
    #            analyzed=analyzed + i.upper()                        
    #         data={'rpu': rpu , 'btext': analyzed }         
    #     return render(request,'base.html', data)
    
    # elif(nl == "on") :               
    #     analyzed=""
    #     for i in Atext:
    #         if i != '\n' and i != '\r':
    #            analyzed=analyzed + i.upper() 
    #         #    analyzed=analyzed                       
    #         data={'rpu': rpu , 'btext': analyzed }         
    #     return render(request,'base.html', data)     
            
              
    # else:
    #     return HttpResponse(" !!! oooo MENTAL MENLTAL BHIA APP NE SUB KUCH KUTTAM KAR DIYA HE  HA HA HA HI HI HI !!! ")    
 
        
 

        return render(request,'base.html')
                    
       
def info(request):
    return render(request,'info.html')
