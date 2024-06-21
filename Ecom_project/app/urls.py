"""
URL configuration for Ecom_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from . form import LoginForm,PasswordResetForm,PasswordChangeForm,SetNewPasswordForm
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetailsView.as_view(),name='product_details'),
    path('products-title/<val>', views.CategoryTitle.as_view(), name='products-title'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update_address/<int:pk>', views.UpdateAddressView.as_view(), name='update_address'),
    path('delete_address/<int:pk>', views.DeleteAddressView.as_view(), name='delete_address'),
    # cart section
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart_items, name='cart'),
    path('remove_cart/<int:prod_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('plus_cart/',views.plus_cart),
    path('minus_cart/',views.minus_cart),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('orders/',views.order_success,name='orders'),
    # User Authentication Section
    path('registration/', views.UserResgistrationView.as_view(), name='registration'),
    path('login/',auth_view.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm),name='login'),
    path('password-change/',auth_view.PasswordChangeView.as_view(template_name="app/pwd_change.html", form_class=PasswordChangeForm,success_url='/password-change-done'),name='change_pwd'),
    path('password-change-done/',auth_view.PasswordChangeDoneView.as_view(template_name="app/pwd_change_done.html"),name='Pwd_change_done'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    #password reset
    path('reset_password/',auth_view.PasswordResetView.as_view(template_name="app/reset_password.html", form_class=PasswordResetForm),name='reset_password'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=SetNewPasswordForm),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),name='password_reset_complete'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ? FOR IMAGE URL CONFIG