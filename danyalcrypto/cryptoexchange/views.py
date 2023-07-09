from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import PurchaseForm, CreateUserForm


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            customer = Customer()
            customer.name = request.POST.get('username')
            customer.email = request.POST.get('username')
            customer.balance = 0
            customer.stockvalue = 0
            customer.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'cryptoexchange/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorroct')

    context = {}
    return render(request, 'cryptoexchange/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    customer = Customer.objects.get(name=request.user.username)
    myorders = Order.objects.filter(customer=customer)
    mystocks = Stock.objects.filter(customer=customer)
    
    context = {'customer':customer, 'myorders':myorders, 'mystocks':mystocks}
    return render(request, 'cryptoexchange/home.html', context)

@login_required(login_url='login')
def profileSettings(request):
    return HttpResponse('Home')

@login_required(login_url='login')
def cryptos(request):
    coins = Coin.objects.all()
    return render(request, 'cryptoexchange/cryptos.html', {'coins':coins})

@login_required(login_url='login')
def orders(request):
    return HttpResponse('Home')

@login_required(login_url='login')
def purchase(request, pk):
    coin = Coin.objects.get(id=pk)
    customer = Customer.objects.get(name=request.user.username)
    order = Order()
    order.coin = coin
    order.customer = customer
    form = PurchaseForm(instance=order)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('coins')
    context = {'form':form}
    return render(request, 'cryptoexchange/purchaseform.html', context)

def buy_from_exchange():
    return True



# Create your views here.
