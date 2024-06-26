from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .form import LoginForm, PasswordResetForm, PasswordChangeForm, SetNewPasswordForm

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('product_details/<int:pk>/', views.ProductDetailsView.as_view(), name='product_details'),
    path('products-title/<val>/', views.CategoryTitle.as_view(), name='products-title'),
    #profile section
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update_address/<int:pk>/', views.UpdateAddressView.as_view(), name='update_address'),
    path('delete_address/<int:pk>/', views.DeleteAddressView.as_view(), name='delete_address'),
    # cart section
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart_items, name='cart'),
    path('remove_cart/<int:prod_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minus_cart/', views.minus_cart, name='minus_cart'),
   # checkout section
    path('CheckoutAddForm/',views.CheckoutAddForm,name="CheckoutAddForm"),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),
    #payment
    #path('order_payment/', views.order_payment, name='order_payment'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('order_success/', views.order_success, name='order_success'),
    # User Authentication
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name='login'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="app/pwd_change.html", form_class=PasswordChangeForm, success_url='/password-change-done/'), name='change_pwd'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="app/pwd_change_done.html"), name='Pwd_change_done'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app/reset_password.html", form_class=PasswordResetForm), name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=SetNewPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
