from django.shortcuts import render
from .models import Pizza,Salads,Noodles,Order

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):

    dests=Pizza.objects.all()
    return render(request,"index.html",{'dests':dests})

def home(request):
    return render(request,"home.html")

def salads(request):
    dests=Salads.objects.all()
    return render(request,"index.html",{'dests':dests})

def login(request):
    return render(request,"login.html")


def noodles(request):
    dests=Noodles.objects.all()
    return render(request,"index.html",{'dests':dests})

def projectPage(request,pk):
    if Pizza.objects.filter(id=pk).exists():
        project=Pizza.objects.get(id=pk)
        context={'project':project}
    elif Noodles.objects.filter(id=pk).exists():
        project=Noodles.objects.get(id=pk)
        context={'project':project}
    elif Salads.objects.filter(id=pk).exists():
        project=Salads.objects.get(id=pk)
        context={'project':project}
    # project=Ecommerce.objects.get(id=pk)
    # context={'project':project}
    return render(request,"home.html",context)
def checkout(request):
    if request.method=="POST":
        items=request.POST.get('items',"")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        zipcode=request.POST.get('zipcode',"")
        total=request.POST.get('total',"")
        order=Order(items=items,total=total,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        order.save()
        send_mail_after_ordered(email)
        return render(request,'success.html')

    return render(request,'checkout.html')
def send_mail_after_ordered(email):
    subject="Your ordered has been succeded"
    message='''<html>
    <body>
        <h1> Your order successfully reached Thanks for reaching out to us Our delivery guy will reach you in a minute</h1>
    </body>
</html>
'''
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list )