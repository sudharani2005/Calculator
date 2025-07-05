from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    result=None
    if request.method=='POST':
        a = int(request.POST.get('num1'))
        b = int(request.POST.get('num2'))
        Op=request.POST.get('Operation')
        if Op=='add':
            result=a+b
        elif Op=='sub':
            result=a-b
        elif Op=='mul':
            result=a*b
        elif Op=='div':
            result=a/b
        else:
            return render(request,'home.html',{'error':'error'})
        #return render(request,'home.html',{'result':result})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})

