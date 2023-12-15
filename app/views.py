from django.db.models import Count
from django.shortcuts import render, redirect, reverse
from django.views import View
from . models import Product, Cart, Wishlist
from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Cart
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from . forms import LoginForm
from .models import Customer
from django.http import JsonResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

# def home(request):
#     return render(request,"app/index.html")

class ProductView(View):
    def get(self, request):
        books = Product.objects.filter(category='BK')
        accessory = Product.objects.filter(category='AR')
        merchandise = Product.objects.filter(category='MC')
        stationary = Product.objects.filter(category='SI')
        electronics = Product.objects.filter(category='EC')
        return render(request, 'app/index.html',
        {'books':books, 'accessory':accessory,'merchandise':merchandise,'stationary':stationary,'electronics':electronics,})

# class CartView(View):
#     def get(self,request):
#         return render(request,"app/cart.html",locals())
#     totalitem = 0
#     if request.user.is_authenticated:
#         totalitem = len(Cart.objects.filter(user=request.user))
#     return render(request,"app/index.html",locals())

# class CartView(View):
#     def get(self,request):
#         return render(request,"app/cart.html",locals())
    
    
class AccountView(View):
    def get(self,request):
        return render(request,"app/account.html",locals())
 
# class AccountView(View):
#     def get(self,request):
#         return render(request,"app/account.html",locals())



class AboutView(View):
    def get(self,request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/about.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail.html",locals())
    
class ProductDetail1(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail1.html",locals())


class ProductDetail2(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail2.html",locals())


class ProductDetail3(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail3.html",locals())   
    
class ProductDetail4(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail4.html",locals())
    
class ProductDetail5(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail4.html",locals())   
    
# women detail
class ProductDetail6(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/productdetail6.html",locals())     

class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        product= Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

# merchandise
# men
def merchandise(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			merchandise = Product.objects.filter(category='MC')
	elif data == 'tshirt' or data == 'hoodie':
			merchandise = Product.objects.filter(category='MC').filter(brand=data)
	elif data == 'below':
			merchandise = Product.objects.filter(category='MC').filter(discounted_price__lt=500)
	elif data == 'above':
			merchandise = Product.objects.filter(category='MC').filter(discounted_price__gt=500)
	return render(request, 'app/merchandise.html', {'merchandise': merchandise, 'totalitem': totalitem})
    
# books
def books(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			books = Product.objects.filter(category='BK')
	elif data == 'below':
			books = Product.objects.filter(category='BK').filter(discounted_price__lt=500)
	elif data == 'above':
			books = Product.objects.filter(category='BK').filter(discounted_price__gt=500)
	return render(request, 'app/books.html', {'books': books, 'totalitem': totalitem})

# assessory
def accessory(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			accessory = Product.objects.filter(category='AR')
	elif data == 'Bag' or data == 'Cover':
			accessory = Product.objects.filter(category='AR').filter(brand=data)
	elif data == 'below':
			accessory = Product.objects.filter(category='AR').filter(discounted_price__lt=500)
	elif data == 'above':
			accessory = Product.objects.filter(category='AR').filter(discounted_price__gt=500)
	return render(request, 'app/accessory.html', {'accessory': accessory, 'totalitem': totalitem})

# stationary
def stationary(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			stationary = Product.objects.filter(category='SI')
	elif data == 'Diary' or data == 'Pen' or data== 'Calendar':
			stationary = Product.objects.filter(category='SI').filter(brand=data)
	elif data == 'below':
			stationary = Product.objects.filter(category='SI').filter(discounted_price__lt=500)
	elif data == 'above':
			stationary = Product.objects.filter(category='SI').filter(discounted_price__gt=500)
	return render(request, 'app/stationary.html', {'stationary': stationary, 'totalitem': totalitem})


# electronics
def electronics(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			electronics = Product.objects.filter(category='EC')
	elif data == 'Mouse' or data == 'Keyboard'  or data == 'Camera'  or data == 'Headphones' or data == 'USB Cable' :
			electronics = Product.objects.filter(category='EC').filter(brand=data)
	elif data == 'below':
			electronics = Product.objects.filter(category='EC').filter(discounted_price__lt=500)
	elif data == 'above':
			electronics = Product.objects.filter(category='EC').filter(discounted_price__gt=500)
	return render(request, 'app/electronics.html', {'electronics':  electronics, 'totalitem': totalitem})

# women
def Women(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			Women = Product.objects.filter(category='WM')
	elif data == 'tshirt' or data == 'hoodie':
			Women = Product.objects.filter(category='WM').filter(brand=data)
	elif data == 'below':
			Women = Product.objects.filter(category='WM').filter(discounted_price__lt=500)
	elif data == 'above':
			Women = Product.objects.filter(category='WM').filter(discounted_price__gt=500)
	return render(request, 'app/Women.html', {'Women':  Women, 'totalitem': totalitem})


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/customerregistration.html",locals())  
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")    
        return redirect("login")
 
        return redirect("login") 

# @method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def  get(self,request):
        return render(request, "app/profile.html",locals())
    def  post(self,request):
        return render(request, "app/profile.html", locals())
    
 
     
        
        return redirect("login")
 
        return redirect("login") 

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def  get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
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
 
  

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    # print(add)
    totalitem = 0
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,'app/address.html',locals())   
 
 
 
 



    # return render(request, "app/customerregistration.html",locals()) 

    
 
 
  
 
    

# @method_decorator(login_required,name='dispatch')
class updateAddress(View):   
    def get(self, request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
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
 
        # return render(request,'app/updateAddress.html',locals())        

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')
 

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount 
    totalamount = amount + 40
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html',locals())
 
 
@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount 
        return render(request,"app/checkout.html",locals())
 
 
@login_required
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
            amount = amount 
        totalamount = amount 
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
        totalamount = amount 
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
        totalamount = amount
        # print(prod_id)
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
 
@method_decorator(login_required,name='dispatch')
class FAQsView(View):
    def get(self,request):
        return render(request,'app/FAQs.html',locals())
    
@method_decorator(login_required,name='dispatch')    
class termsView(View):
    def get(self,request):
        return render(request,'app/terms.html',locals())
    
    from django.shortcuts import redirect


@login_required    
def search(request):
    query = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())

def add_to_wishlist(request):
    if request.method == "POST":
        print(request.POST)
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Wishlist(user=user,product=product).save()
    return redirect('/wishlist')
 


def show_wishlist(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    return render(request, 'app/addtowishlist.html',locals())

def remove_wishlist(request):
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
        totalamount = amount
        # print(prod_id)
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
 


    
    

    






    
                   # <div class="text-sm flex flex-row gap-2 ml-2 text-black items-center justify-center">
                       # <i class="fa-regular fa-user rounded-lg p-2"></i>  
                        #<div>Welcome ,User</div>
                        #<div class="relative inline-block">
                         #   <i id="userIcon" class="fa fa-caret-down text-black rounded-lg p-2 cursor-pointer"></i>
                          #  <div id="dropdown" class="hidden absolute right-0 mt-2 space-y-2 bg-white border border-black rounded-md shadow-lg z-10">  
                           #     <a href="{% url 'profile' %}" class="block px-4 py-2 text-gray-800 hover:bg-gray-100">My Account</a>
                            #    <a href='/' class="block px-4 py-2 text-gray-800 hover:bg-gray-100 text-red-700">Logout</a>
                            #</div>
                        #</div>
                        
                    #</div>
                    #<a href="{% url 'customerregistration' %}" class="bg-blue-700 hover:bg-blue-800 text-white px-4 py-2 rounded mr-4">Login/Signup</a>
                 
                    
                #</div>#
    
    
    
    
    
