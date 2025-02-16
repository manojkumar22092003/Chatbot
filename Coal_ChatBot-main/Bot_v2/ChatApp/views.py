from django.shortcuts import render
from django.http import HttpResponse
from .models import signup

def home(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        
        obj = signup()
        obj.Firstname=firstname
        obj.Lastname=lastname
        obj.Email=email
        obj.Password=password
        obj.save()
    return render(request,'index.html')
def main(request):
    return render(request,('main.html'))

def validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        users = signup.objects.filter(Email=username, Password=password)
        
        if users.exists():
            return render(request, 'main.html')
        else:
            return HttpResponse('Invalid username or password')
    
    return render(request, 'signin.html')