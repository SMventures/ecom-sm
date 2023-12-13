from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
urlpatterns = [
  
    # path("",views.home),
    path('',views.ProductView.as_view(), name='home'),
    
    path('merchandise/', views.merchandise, name='merchandise'),
    path('merchandise/<slug:data>', views.merchandise, name='merchandisedata'),
    
    path('accessory/', views.accessory, name='accessory'),
    path('accessory/<slug:data>', views.accessory, name='accessorydata'),
    
    path('books/', views.books, name='books'),
    path('books/<slug:data>', views.books, name='booksdata'),
    
    path('stationary/', views.stationary, name='stationary'),
    path('stationary/<slug:data>', views.stationary, name='stationarydata'),

    path('electronics/', views.electronics, name='electronics'),
    path('electronics/<slug:data>/', views.electronics, name='electronicsdata'),
    
    
  
    
    path("about", views.AboutView.as_view(),name="about"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path("add-to-cart/", views.add_to_cart,name="add-to-cart"),
    path("cart/", views.show_cart,name="showcart"),
    path("checkout/", views.checkout.as_view(),name="checkout"),
    
    path("search/", views.search,name="search"),
    
    
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
   
    
    
    path("FAQs/", views.FAQsView.as_view(), name="FAQs" ),
    path("terms/",views.termsView.as_view(), name="terms"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
 
 
 
    
    
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),   
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_done.html',form_class=MyPasswordResetForm),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordResetForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_complete.html',form_class=MyPasswordResetForm),name='password_reset_complete'),
 
    path("profile/", views.ProfileView.as_view(), name="profile"),
 
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name="login"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=MyPasswordResetForm), name='password_reset'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)