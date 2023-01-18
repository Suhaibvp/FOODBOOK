from email.mime import image
from django.http import HttpResponse
from django.shortcuts import render
from unittest import result
from urllib import request
from django.shortcuts import redirect
from django.db.models import Count
from .models import*
from  django.core.files.storage import FileSystemStorage
import datetime
# index page
def index(request):
    return render(request,'index.html') 
def indexx(request):
    return render(request,'index.html') 

# for register
def register(request):
    return render(request,'register.html') 
def addregister(request):
    if request.method=="POST":
        fullname=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        registration=customer(full_name=fullname,contact=contact,email_address=email,username=username,password=password,confirm_password=confirmpassword)
        registration.save()
        return render(request,'register.html',{'success':'Register Successfully'})
        
# for login
def login(request):
    return render(request,'login.html')         

def addlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password =='admin':
        request.session['logintdetail'] = username
        request.session['admin'] = 'admin'
        return render(request, 'index.html')

    elif customer.objects.filter(username=username,password=password).exists():
        userdetails=customer.objects.get(username=request.POST['username'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.full_name

            request.session['username'] = username

            request.session['user'] = 'user'

            return render(request,'index.html')

    else:
        return render(request, 'login.html', {'status': 'Invalid Username or Password'})



# approvel
def paid(request):
    user=order.objects.filter(order_status='approved')
    return render(request,'paid.html',{'result':user})   

      
# logout
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
     del request.session[key]
    return redirect(index) 

# add foods
def addfood(request):
    return render(request,'addfood.html') 
def addfoods(request):
    if request.method=="POST":
        foodtype=request.POST.get('foodtype')
        price=request.POST.get('price')
        foodname=request.POST.get('foodname')
        myfile=request.FILES['image']
        print(myfile)
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        starttime = datetime.datetime.now()

        reg=food(foodtype=foodtype,price=price,image=myfile,foodname=foodname,starttime=starttime)
        reg.save()
        return render(request,'addfood.html')

# view foods
def viewfoodc(request): 
    users=food.objects.all()
    return render(request,'viewfoodc.html',{'result':users})
  
def viewfood(request):
    user=food.objects.all()
    return render(request,'viewfood.html',{'result':user}) 

# cancel food
def delete(request,id):
    member = food.objects.get(id=id)
    member.delete()
    return redirect(viewfood)

def update(request,id):
    upt=food.objects.get(id=id)
    return render(request,'update.html',{'result':upt})   

def updates(request,id):
    if request.method=="POST":
        foodtype=request.POST.get('foodtype') 
        price=request.POST.get('price')
        foodname=request.POST.get('foodname')
        myfile=request.FILES['image']
        print(myfile)
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        stays=food(foodtype=foodtype,price=price,image=myfile,foodname=foodname,id=id)
        stays.save()
        return redirect(viewfood)   

def profile(request):
    tem=request.session['uid']
    vpro=customer.objects.get(id=tem)
    return render(request,'profile.html',{'result':vpro})  

def vieworder(request):
    user=order.objects.filter(order_status='pending')
    return render(request,'vieworder.html',{'result':user}) 

def viewcart(request):
    temp=request.session['uname']
    user=order.objects.filter(customer_id=temp,order_status='approved')
    return render(request,'viewcart.html',{'result':user}) 
    
def vieworderr(request):
    temp=request.session['uname']
    user=order.objects.filter(customer_id=temp)
    return render(request,'viewpendingorder.html',{'result':user}) 
        
    
def totalorder(request):

    user=order.objects.all()

    dat=dict()

    for i in user:
        if i.menu_id in dat.keys(): 
            q=int(i.quantity)+int(dat[i.menu_id])
            dat[i.menu_id]=q
            #print(q)
        else:
            dat[i.menu_id]=i.quantity
    print(dat)



    return render(request,'totalfood.html',{'result':user}) 





    
def orderfood(request):
    return render(request,'orderfood.html') 

def addorder(request):
    b=request.session['uname']
    if request.method=="POST":
        menuid=request.POST.get('menuid')
        amount=int(request.POST.get('price'))
        orderstatus=request.POST.get('status')
        quantity=int(request.POST.get('quantity'))
        c=amount*quantity
        
        reg=order(total_amount=c,order_status=orderstatus,quantity=quantity,menu_id=menuid,customer_id=b)
        reg.save()
        return redirect(viewfoodc)   
def orderss(request,id):
    upt=food.objects.get(id=id)

    return render(request,'orderfood.html',{'result':upt})

def payment(request,id):
    user=order.objects.get(id=id)
    return render(request,'payment.html',{'result':user})   

def viewcustomerorder(request,id):
    upt=order.objects.get(id=id)
    return render(request,'viewfoodorder.html',{'result':upt})
    
def paidorder(request,id):
    upt=order.objects.get(id=id)

    return render(request,'paidorder.html',{'result':upt})



def viewpayment(request):
    return render(request,'viewpayment.html')     
    



def paided(request):
    if request.method=="POST":
        token=request.POST.get('tokenid')
        upt=order.objects.get(id=token)

        a=upt.customer_id
        b=upt.menu_id
        c=upt.total_amount
        d=upt.quantity
        status='paid'
        reg=order(total_amount=c,order_status=status,quantity=d,menu_id=b,customer_id=a,id=token)
        reg.save()
        return redirect(paid)

def approved(request,id):
    upt=order.objects.get(id=id)
    a=upt.customer_id
    b=upt.menu_id
    c=upt.total_amount
    d=upt.quantity
    status='approved'
    reg=order(total_amount=c,order_status=status,quantity=d,menu_id=b,customer_id=a,id=id)
    reg.save()
    return redirect(vieworder)

def homeback(request):
    return render(request,'index.html')     
    

    
    
