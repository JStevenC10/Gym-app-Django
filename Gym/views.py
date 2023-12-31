import random

from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import ClientGymForm, LoginForm
from .messages import MOTIVATION, NOT_PAYED, NOT_PAYED_2
from .models import ClientGym

# Create your views here.

# HOME APP
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})

# CLIENTS TABLE AND SEARCH A CLIENT 
def all_clients(request, *args, **kwargs):
    # ALL CLIENTS
    if request.method == 'GET':
        clients = ClientGym.objects.all()
        if clients:
            return render(request, 'all_clients.html', {'clients': clients})
        else:
            return render(request, 'all_clients.html')
    # SEARCH A CLIENT WITH POST METHOD 
    else:
        search = request.POST['search']
        clients = ClientGym.objects.filter(Q(name__icontains=search) | Q(surname__icontains=search))
        if clients:
            return render(request, 'all_clients.html', {'clients': clients})
        else:
            return render(request, 'all_clients.html')


# REGISTER NEW CLIENT GYM
def register(request, *args, **kwargs):
    if request.method == 'POST':
        new_client = ClientGymForm(data=request.POST)
        if new_client.is_valid():
            new_client.save()
            return redirect(to=login)
        else:
            return redirect(to=register)
    else:
        form = ClientGymForm
        return render(request, 'register.html', {'form': form})

# SEE INFO CLIENT GYM
def login(request, *args, **kwargs):
    if request.method == 'POST':
        client = ClientGym.objects.filter(cc=request.POST['cc']).first()
        if client:
            return redirect('welcome', cc=client.cc, name=client.name)
        else:
            return redirect(to=login)
    else:
        form = LoginForm
        return render(request, 'login.html', {'form': form})

# WELCOME FOR CLIENTS GYM
def welcome(request, *args, **kwargs):
    phrase = random.choice(MOTIVATION)
    client = ClientGym.objects.filter(cc=kwargs['cc']).first()
    if client:
        days = client.days_available()
        context = {
            'client':client,
            'phrase': phrase,
            'days': days
        }
        # MESSAGE FOR CLIENT NOT PAYED
        if not client.payed:
            context['phrase'] = random.choice([NOT_PAYED, NOT_PAYED_2])
        return render(request, 'welcome.html', context)
    else:
        return redirect(to=login)
    
# PAY NEW MONTH
def pay_month(request, *args, **kwargs):
    client = ClientGym.objects.filter(cc=kwargs['cc']).first()
    if client.payed:
        return redirect('welcome', cc=client.cc, name=client.name)
    else:
        client.payed = True
        client.restart_dates()
        client.save()
        return redirect('welcome', cc=client.cc, name=client.name)

# DELETE CLIENT
def delete_client(request, *args, **kwargs):
    client = ClientGym.objects.filter(cc=kwargs['cc']).first()
    if client:
        client.delete()
        return redirect(to=all_clients)
    else:
        return redirect(to=all_clients)