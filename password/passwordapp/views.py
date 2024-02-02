from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'passwordapp/index.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upercase',''):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special',''):
        characters.extend(list('@!&%$?/()'))
    if request.GET.get('number',''):
        characters.extend(list('0123456789'))
        
    length = int(request.GET.get('length',20))
    thepassword=''
    
    for x in range(length):
        thepassword+=random.choice(characters)
        
        
    return render(request, 'passwordapp/password.html',{'password':thepassword})

def about(request):
    return render(request,'passwordapp/about.html')

def contact(request):
    return render(request,'passwordapp/contact.html')