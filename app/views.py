from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category = 'TW')
  bottomwears = Product.objects.filter(category = 'BW')
  mobiles = Product.objects.filter(category = 'M')
  return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles})

class ProductDetailView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})
 
def Topwear(request, data=None):
    if data == None:
        top = Product.objects.filter(category='TW')
    elif data == 'Levis' or data == 'Lee':
        top = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
      top = Product.objects.filter(category = 'TW').filter(discounted_price__lt=500)
    elif data == 'above':
      top = Product.objects.filter(category = 'TW').filter(discounted_price__gt=500)

    return render(request, 'app/Topwear.html', {'top': top})

def logout_page(request):
    logout(request)
    return redirect('login')

def Bottomwear(request, data=None):
    if data == None:
        bottom = Product.objects.filter(category='BW')
    elif data == 'Levis' or data == 'Lee':
        bottom = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
      bottom  = Product.objects.filter(category = 'BW').filter(discounted_price__lt=500)
    elif data == 'above':
      bottom = Product.objects.filter(category = 'BW').filter(discounted_price__gt=500)

    return render(request, 'app/Bottomwear.html', {'bottom': bottom})


def mobile(request, data = None):
  if data == None:
   mobiles = Product.objects.filter(category='M')
  elif data == 'Redmi' or data == 'Samsung':
   mobiles = Product.objects.filter(category = 'M').filter(brand = data)
  elif data == 'below':
    mobiles  = Product.objects.filter(category = 'M').filter(discounted_price__lt=25000)
  elif data == 'above':
    mobiles  = Product.objects.filter(category = 'M').filter(discounted_price__gt=25000)

  return render(request, 'app/mobile.html',{'mobiles':mobiles})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def login(request):
#  return render(request, 'app/login.html')

class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html',{'form':form})
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'User registered successfully!!')
      form.save()
    return render(request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request, 'app/profile.html', {'form':form})
