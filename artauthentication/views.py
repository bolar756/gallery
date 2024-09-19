from django.shortcuts import render , redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from appgallery.models import Shop, Category ,ArtItems
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def Login(request):
    if request.method=="POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        auth.login(request,user)
        return redirect('home')
    else:    
       return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method =="POST": 
       username = request.POST['name']
       email = request.POST['email']
       password1 = request.POST['password']
       password = request.POST['password1']
       if password==password and len(password) > 7:
           user = User.objects.create_user(username=username, email=email, password=password)
           user.save()
           user = authenticate( request, username=username, password=password)
           auth.login(request,user)
           if  user != None:
               auth.login(request,user)
               return redirect('home')
           else:
               return render(request,'login.html')
       else:
           return render(request,'signup.html')        
    else:       
       return render(request,'signup.html')
    
def createproduct(request):
   if request.method == "POST":
        shoper = Shop.objects.get(owner=request.user)
        name = request.POST['name']
        bio = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        categ = request.POST['category']
        cre=Category.objects.get(name=categ)
        Prod = ArtItems.objects.create(name=name, description=bio, price=price, category=cre ,owner=shoper, image=image)
        Prod.save()
        return redirect(f'shop/{shoper.name}')
   else:
      category = Category.objects.all()
      return render(request,'product.html',context={'category':category})
   
def deleteproduct(request , pk):
    art=ArtItems.objects.get(pk=pk)
    art.delete()
    try:
      shops = Shop.objects.get(owner=request.user)
      artitems = ArtItems.objects.filter(owner= shops)
      return render(request,'shop.html', context={'shops': shops, 'artitems':artitems})    
    except Exception as e:
        return render(request,'shop.html' ,context={'e':e})

@login_required(login_url='login')    
def createshop(request):
      if request.user.is_authenticated:
       try: 
        shoper = Shop.objects.get(owner=request.user)
        return redirect(f'shop/{shoper.name}') 
       except Exception: 
           shopname = request.POST['shopname']
           shopbio = request.POST['shopbio']
           shoplogo = request.FILES['shoplogo']
           flink=request.POST['flink']
           ilink=request.POST['ilink']
           wlink=request.POST['wlink']
           seed = Shop()
           shop=Shop.objects.create(name=shopname,shop_bio=shopbio, owner=request.user,
                            instagram_link=ilink, whatsapp_link=wlink, facebook_link=flink , shop_logo=shoplogo )
           shop.save()
           shope = Shop.objects.get(owner=request.user)
           return redirect(f'shop/{shope.name}')

@login_required(login_url='login')    
def shopform(request):
   if request.method == "POST":
           shopname = request.POST['shopname']
           shopbio = request.POST['shopbio']
           shoplogo = request.FILES['shoplogo']
           flink=request.POST['flink']
           ilink=request.POST['ilink']
           wlink=request.POST['wlink']
           seed = Shop()
           shop=Shop.objects.create(name=shopname,shop_bio=shopbio, owner=request.user,
                            instagram_link=ilink, whatsapp_link=wlink, facebook_link=flink , shop_logo=shoplogo )
           shop.save()
           shope = Shop.objects.get(owner=request.user)
           return redirect(f'shop/{shope.name}')

def update_shop(request):
    if request.method == "POST":
        shopname = request.POST['shopna']
        shopdescr = request.POST['shopdescr']
        try:
          shop = Shop.objects.get(owner=request.user)
        #   shop.shop_logo=shopimage
          shop.name = shopname
          shop.shop_bio = shopdescr
          shop.save()
          return redirect(f'shop/{shop.name}')
        except Exception as e:
            return redirect('/')  
                