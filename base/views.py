from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Place,Messages
from .forms import Placeform,placeformhtml
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

places=[
]
user1=[]
def test(request):
  
 
  
  if request.GET.get('q') != None:
    q=request.GET.get('q')
    places = Place.objects.filter(name__contains=q)
  else :
    places = Place.objects.filter()
  context={
     'place':places,
     'user1':user1,
     
   }
  return render(request,'home.html',context)

def messagepage(request,pk):
  places1=get_object_or_404(Place,id=pk)
  messages1=places1.messages_set.all()
  context={ 
  'places1':places1,
  'message1':messages1
  }
  return render(request,'messagepage.html',context)

@login_required(login_url="userlogin")
def placecreate(request):
 form=Placeform()
 if request.method=='POST':
   form=Placeform(request.POST)
   if form.is_valid:
    
     place_save=Place.objects.create(
       user=request.user,
       name=request.POST.get('name'),
       desc=request.POST.get('desc')
     )
     
     return redirect('home')
 context={'form':form,
          'user1':user1
   
 }
 return render(request,'placecreate.html',context)

def cr(request):
  return render(request,'cr.html')

@login_required(login_url="userlogin")
def deletepage(request,pk):
  p=get_object_or_404(Place,id=pk)
  if request.user != p.user:
    return HttpResponse('not yours')
  if request.method =='POST':
    p.delete()
    return redirect('home')
  return render(request,'deletepage.html',{'p':p})


def user_login(request):
  page=True
  if request.method=='POST':
    username = request.POST.get('username', '')
    password=request.POST.get('password', '')
  
    user=User.objects.get(username=username)
    print(username)
        
   
       
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      user1=user
      return redirect('home')



        
  context={
    'page':page,
  }
  return render(request,'user_login.html',context)
  

def user_logout(request):
  logout(request)
  return render(request,'home.html')

def user_register(request):
  page=False
  context={
    'page':page,
  }
  return render(request,'user_login.html',context)