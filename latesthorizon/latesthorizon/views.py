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
# def contact(request):
#     return render(request,'contact.html')
def uploader(request):
    return render(request,'uploader.html')
def base(request):
    return render(request,'base.html')
def contact(request):
    return render(request,'contact.html')
def fonts(request):
    return render(request,'fonts.html')


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

# def analyze(request):   
#     djtext = request.POST.get('text','default')   
#     removepunc = request.POST.get('removepunc','off')
#     # fullcaps = request.POST.get('fullcaps','off')
#     # newlineremover = request.POST.get('newlineremover','off')
#     # extraspaceremover = request.POST.get('extraspaceremover','off')   
#     if removepunc == "on":
#         punctuations = '''!()-[]{,};:'"\,<>./?@#$%^&*_~'''
#         analyzed=""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
#     return render(request, 'analyze.html', params)
    
    
    # elif(fullcaps=="on"):
    #     analyzed=""
    #     for char in djtext:
    #         analyzed = analyzed + char.upper()
    #     params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}       
    #     return render(request, 'analyze.html', params)
    
    # elif(extraspaceremover=="on"):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if not(djtext[index] == " " and djtext[index+1]==" "):
    #             analyzed = analyzed + char
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}       
    #     return render(request, 'analyze.html', params)
    
    # elif (newlineremover == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "\n":
    #             analyzed = analyzed + char
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}        
    #     return render(request, 'analyze.html', params)
    
    # else:
    #     return HttpResponse("Error")


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{,};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {"purpose":'Removed NewLines',"analyzed_text":analyzed}
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)























# def info(request):  
#     Atext=request.GET.get('text','default')
#     rpu=request.GET.get('rpu','off')
#     upper=request.GET.get('upper','off') 
#     print(rpu)
#     print(Atext)
#     if rpu == "on" :  
#         punctuations = ''' ?  , : ,   ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] , @ ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
#         analyzed=""
#         for I in Atext:
#             if I not in punctuations:
#                analyzed=analyzed+I 
#         data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'info.html',data)
    
#     elif upper == "on":
#         punctuations = ''' ?  , : ,   ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] , @ ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
#         analyzed=""
#         for I in Atext:
#             if I not in punctuations:
#                analyzed=analyzed + I.upper() 
#         data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'info.html',data)    
    
#     else:
#         return HttpResponse(" sab ghalat kar diya khaotay tou hay hi AQAL say paidal ")     
    
    





   
# def contact(request):  
#     Atext=request.POST.get('text','default')
#     rpu=request.POST.get('rpu','off')
#     upper=request.POST.get('upper','off')
#     nl=request.POST.get('nl','off')  
    
#     if rpu == "on" :
        
#         punctuations = ''' ? ` , : , @  ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] ,  ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
#         analyzed=""
#         for i in Atext:
#             if i not in punctuations:
#                analyzed=analyzed+i 
#         data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'contact.html', data)
#     elif(upper == "on") :
#         punctuations = '''?`,:,@;,%^<<,,,>>>{..!!!|“”,_-(),,[],,*,\\\}::"""'~,/,,#,$,&''' 
#         analyzed=""
#         for i in Atext:
#             if i not in punctuations:
#                analyzed=analyzed + i.upper()                        
#             data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'contact.html', data)
    
#     elif(nl == "on") :               
#         analyzed=""
#         for i in Atext:
#             if i != '\n' and i != '\r':
#                analyzed=analyzed + i.upper() 
#             #    analyzed=analyzed                       
#             data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'contact.html', data)     
            
              
#     else:
#         return HttpResponse(" !!! oooo MENTAL MENLTAL BHIA APP NE SUB KUCH KUTTAM KAR DIYA HE  HA HA HA HI HI HI !!! ")    
 
        
 

#         return render(request,'contact.html')
                    
       
def info(request):
    return render(request,'info.html')
