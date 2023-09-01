from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import*
from .forms import*


# Create your views here.
def index(request):
     if request.method == 'POST':
        return render(request,'index.html')
     else:
       
      return render(request,'index.html')
    

def register (request):
    if request.method == 'POST':
        print('POSTED')
        First_name = request.POST['First_name']
        Last_name= request.POST['Last_name']
        Genda = request.POST['Date_Of_Birth']
        Country = request.POST['Country']
        Town= request.POST['Town']
        District = request.POST['District']
        Zip_code= request.POST['Zip_code']
        Phone_Number1 = request.POST['Phone_Number1']
        Phone_Number2= request.POST['Phone_Number2']
    
        context = [First_name,Last_name,Genda,Country,Town,District,Zip_code,Phone_Number1,Phone_Number2]
        print(context)
    return render(request,'register.html')
    