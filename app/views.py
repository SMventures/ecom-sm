from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Cart
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from . forms import LoginForm
from .models import Customer
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"app/index.html")

class CartView(View):
    def get(self,request):
        return render(request,"app/cart.html",locals())
    
class ItemView(View):
    def get(self,request):
        return render(request,"app/item.html",locals())
    
class AccountView(View):
    def get(self,request):
        return render(request,"app/account.html",locals())
    

class AboutView(View):
    def get(self,request):
        return render(request,"app/about.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
    
class CategoryView(View):
    def get(self,request,val):
        product= Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())  
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")    

     
        
        return redirect("login") 

class ProfileView(View):
    def  get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def  post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")    
            
        return render(request, 'app/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    print(add)
    return render(request,'app/address.html',locals())   


    return render(request, "app/customerregistration.html",locals()) 

    # return render(request, "app/customerregistration.html",locals()) 



class updateAddress(View):   
    def get(self, request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name= form.cleaned_data['name']
            add.locality= form.cleaned_data['locality']
            add.city= form.cleaned_data['city']
            add.mobile= form.cleaned_data['mobile']
            add.state= form.cleaned_data['state']
            add.zipcode= form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulation Profile Updated Successfully")
        else:
            messages.warning("Invalid Input data")

        return redirect("address")        

        return render(request,'app/updateAddress.html',locals())        

def add_to_cart(request): 
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'app/addtocart.html',locals())


class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        return render(request,"app/checkout.html",locals())



def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        # print(prod_id)
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

class FAQsView(View):
    def get(self,request):
        return render(request,'app/FAQs.html',locals())
    


    
    
    
    
    
