from django.shortcuts import render

# Create your views here.
def friends(request):
    return render(request,'h1.html')

def indianteam(request):
    return render(request,'indiateam.html')

def virat(request):
    return render(request,'virat.html')

def rohit(request):
    return render(request,'rohit.html')

def kl(request):
    return render(request,'kl.html')

def bumrah(request):
    return render(request,'bumrah.html')

def hardik(request):
    return render(request,'hardik.html')

def siraj(request):
    return render(request,'siraj.html')