from django.shortcuts import render
from gun2.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def c(request):
    return render(request, 'c.html')
def c1(request):
    return render(request, 'c1.html')
def c2(request):
    return render(request, 'c2.html')
def c3(request):
    return render(request, 'c3.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        desc = request.POST.get('desc')

        contact = Contact(name = name, state=state, email = email, phone = phone, lastname = lastname, city = city, zip = zip, desc = desc, date = datetime.today())
        contact.save()

        messages.success(request, 'Your Contact Details has been sent..')
    return render(request, 'contact.html')


