from django.shortcuts import render
from django.views import View
from urllib import request
from django.http import HttpResponse

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
    
class DetailView(View):
    def get(self,request):
        return render(request,"app/product-details.html",locals())