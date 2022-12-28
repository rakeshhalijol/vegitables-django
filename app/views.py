from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Vegitable,reviews,Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    veg = Vegitable.objects.all()
    return render(request,'index.html',{'veg':veg})

def signin(request):
    if request.method == 'POST':
        sname = request.POST.get('sname','')
        semail = request.POST.get('semail', '')
        spass1 = request.POST.get('spass1', '')
        spass2 = request.POST.get('spass2', '')
        if spass1 == spass2:
            retrive_user = User.objects.filter(username = sname)
            if len(retrive_user) == 0:
                retrive_email = User.objects.filter(email=semail)
                if len(retrive_email) == 0:
                    create = User.objects.create_user(username=sname,email=semail,password=spass1)
                    messages.success(request,"Successfully user created")
                    return redirect('login')
                else:
                    messages.error(request,'Email already exists')
                    return redirect('signin')
            else:
                messages.error(request, 'Username already exists')
                return redirect('signin')
        else:
            messages.error(request, 'Password missmatch')
            return redirect('signin')
    else:
        return render(request,'sign.html')

def login(request):
    if request.method == "POST":
        lname = request.POST.get('lname', '')
        lpass = request.POST.get('lpass', '')
        user = auth.authenticate(username = lname,password = lpass)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect(('login'))
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
#(#redirect_field_name='/login/')
# @login_required
def show(request,id):
    if request.user.is_authenticated:
        retrive = Vegitable.objects.filter(id = id)
        review = reviews.objects.filter(item = retrive[0])
        return render(request,'show.html',{'retrive':retrive[0],'reviews':review})
    else:
        messages.error(request,'login first before moving to further')
        return redirect('/login/')

def review(request,id):
    if request.method == "POST":
        get_text = request.POST.get('review_section', '')
        user = request.user
        item = Vegitable.objects.filter(id=id)
        if get_text:
            if item:
                create = reviews.objects.create(user = user,item = item[0],review = get_text)
                create.save()
                messages.success(request,'Thank you reviewing')
                return redirect(f'/show/{item[0].id}')

def cart(request,id):
    retrive = Vegitable.objects.filter(id = id)
    check_cart = Cart.objects.filter(item=retrive[0])
    user = request.user
    if len(check_cart) == 0:
        create = Cart.objects.create(user=user,item=retrive[0],price=retrive[0].price)
        create.save()
    else:pass
    get_user_data = Cart.objects.filter(user=user)
    return render(request,'order.html',{'retrive':get_user_data})

def confirm(request):

    messages.success(request,'Your order placed succesfully check notifications for further trackings')
    return redirect('/')

def shop(request):
    return redirect('/')

def update_quantity(request,id):
    read_quantity = request.POST.get('quantity','')
    update_query = Cart.objects.filter(id=id).update(quntity=read_quantity)

    return HttpResponse("updated")
