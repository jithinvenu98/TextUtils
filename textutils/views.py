
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyser(request):
    
    djtext=request.POST.get('text','off')

    removepunc=request.POST.get('removepunc','off')

    fullcaps = request.POST.get('fullcaps','off')

    newlineremover = request.POST.get('newlineremover','off')

    extraspaceremover = request.POST.get('extraspaceremover','off')

    charcount = request.POST.get('charcount','off')

    
    
    if (removepunc=="on"):

     punctuations = '''()-[]{};:'".\/,<>@#$%^&*+?'''
     analyse= ""
     for char in djtext:
        if char not in punctuations:
            analyse=analyse+ char
        params={'purpose':'Removed punctutions','analysed_text':analyse}
        djtext= analyse
     

    elif(fullcaps=="on"):
     
       analyse=""
       for char in djtext:
        analyse= analyse + char.upper()
        
        params={'purpose':'change to Fullcaps','analysed_text':analyse}
        djtext= analyse
        
    
    elif(newlineremover=="on"):
    
     analyse=""
     for char in djtext:
          if char !="\n":
             analyse=analyse+char


     params={'purpose':'remove newline','analysed_text':analyse}
     djtext= analyse 


    elif(extraspaceremover=="on"):
        analyse = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyse = analyse + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analyse}

        djtext=analyse
        
             
    elif(charcount=="on"):
     analyse=''
     for char in djtext:
       analyse=str(len(djtext))

     params={'purpose':'charcount','analysed_text':analyse}
     djtext = analyse
     


    else:
     return HttpResponse("Error")
     
    return render(request,'analyser.html',params)
    
