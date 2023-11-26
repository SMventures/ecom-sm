from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm
urlpatterns = [
    path("",views.home),
    path("cart", views.CartView.as_view(),name="cart"),
    # path("item", views.ItemView.as_view(),name="item"),
    path("account", views.AccountView.as_view(),name="account"),
    path("about", views.AboutView.as_view(),name="about"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path("add-to-cart/", views.add_to_cart,name="add-to-cart"),
    path("cart/", views.show_cart,name="showcart"),
    path("checkout/", views.show_cart,name="checkout"),
    
    
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    

   
