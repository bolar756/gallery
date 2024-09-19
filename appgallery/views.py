from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models import ArtItems , Shop , Category
import random, json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    lists=ArtItems.objects.all()
    stern = lists[:10]
    if request.method == "POST":
     try:
       shops = Shop.objects.get(owner=request.user) 
       cat = Category.objects.all()
       if shops:
          context={'stern':stern,"lists":lists[:40],'shops':shops,'cat':cat }
          return render(request,'index.html',context)
       else:
         context={'stern':stern,"lists":lists[:40] }
         return render(request,'index.html',context)
     except Exception as e:
       stern = random.choice(lists)
       context={'stern':stern,"lists":lists[:40],'e':e}
       return render(request,'index.html',context)
    else:
       context={'stern':stern,"lists":lists[:40]}
       return render(request,'index.html',context)

def profile(request):
    try: 
       shops = Shop.objects.get(owner=request.user)
       return render(request,'profile.html', context={'shops':shops})
    except Exception as e:
        return render(request,'profile.html' ,context={'e':e})

def shop(request, name):
    if request.user.is_authenticated:
     try:
      shops = Shop.objects.get(name=name)
      artitems = ArtItems.objects.filter(owner= shops)
      if shops.owner != request.user:
         return redirect ('createshop')
      else:
       return render(request,'shop.html', context={'shops': shops, 'artitems':artitems})    
     except shops.DoesNotExist():
         return redirect ('profile')
    else:
        return redirect('/')
    

def user_shop(request , name):    
    try:
         shops = Shop.objects.get(name=name)
         artitems = ArtItems.objects.filter(owner= shops)
         return render(request,'shopview.html', context={'artitems':artitems,'shops':shops})
    except Exception as e:
       return render(request,'shopview.html', context={})
    
def update_profile(request):
     if request.method=="POST":
       user = User.objects.get(username=request.user)
       lat_name = request.POST['last_name']
       fist_name = request.POST['first_name']
       email= request.POST['email']
       try:
            user.last_name=lat_name
            user.first_name=fist_name
            user.email=email
            user.save()
            return redirect('profile')    
       except Exception as e:
           return redirect('profile')
     else:
         return redirect('profile')
     
def search(request):
   if request.method == "POST":
       searc = request.POST['search']
       cate = Category.objects.get(name = searc)
       arts = ArtItems.objects.filter(category = cate)
       num_arts = arts.count()
       return render ( request, 'search.html', {'arts':arts,'num_arts':num_arts})
   else:
      return render (request, 'search.html')
   