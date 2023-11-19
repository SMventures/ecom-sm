from django.urls import path
from .import views

urlpatterns = [
    path("",views.home),
    path("cart", views.CartView.as_view(),name="cart"),
    path("item", views.ItemView.as_view(),name="item"),
    path("account", views.AccountView.as_view(),name="account"),
    path("product-details", views.DetailView.as_view(),name="product-details"),
]

