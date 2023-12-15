from django.contrib import admin
from . models import Cart, Customer, Product, Wishlist
from . models import Cart, Customer, Product

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','brand','Availability','discounted_price','category','product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','user','locality','city','state','zipcode','mobile']
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']    
        
    
