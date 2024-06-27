from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Products, Customers, Cart, Payment, OrderPlaced
from django.db.models import Count, Q
from .form import UserRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import numpy as np
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .constants import PaymentStatus 
from django.utils.decorators import method_decorator

# home page
def index(request):
    return render(request, 'app/index.html')

# about page
def about(request):
    return render(request, 'app/about.html')

# contact page
def contact(request):
    return render(request, 'app/contact.html')

# Retrieve products based on a specific category value and render them in a template.
class CategoryView(View):
    def get(self, request, val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, 'app/products.html', locals())

# product title
class CategoryTitle(View):
    def get(self, request, val):
        product = Products.objects.filter(title=val)
        title = Products.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/products.html', locals())

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        return render(request, 'app/product_detail.html', locals())

# User registration form
class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'app/registration.html', locals())

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
            return redirect('login')
        else:
            messages.warning(request, "Invalid input")
        return render(request, "app/registration.html", locals())

# Customer Profile
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customers(user=user,name=name,locality=locality,city=city,phone=phone,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congradulation ! Profile saved successfully")
        else:
            messages.warning(request,"invalid input ")
        return render(request,'app/profile.html',locals())

# Display the user address

def address(request):
    add = Customers.objects.filter(user=request.user)
    return render(request, 'app/user_address.html', locals())

# Update address

class UpdateAddressView(View):
    def get(self, request, pk):
        add = get_object_or_404(Customers, pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/update_address.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST, instance=get_object_or_404(Customers, pk=pk))
        if form.is_valid():
            form.save()
            messages.success(request, "Details updated successfully")
        else:
            messages.warning(request, "Invalid input")
        return render(request, 'app/update_address.html', locals())

# Delete address

class DeleteAddressView(View):
    def get(self, request, pk):
        add = get_object_or_404(Customers, pk=pk)
        add.delete()
        messages.success(request, "Address deleted successfully")
        return redirect('address')

# Add to cart

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/cart')

# Show cart items

def show_cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    amount = np.sum([item.total_price for item in cart_items])
    total_amount = amount + 40
    return render(request, 'app/cart.html', locals())

# Remove from cart

def remove_from_cart(request, prod_id):
    product = get_object_or_404(Products, id=prod_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.delete()
    return redirect('/cart')

# Quantity plus in cart

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_object = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_object.quantity += 1
        cart_object.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discount_price for item in cart)
        total_amount = amount + 40
        data = {
            'quantity': cart_object.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)

# Minus cart
@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_object = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if cart_object.quantity > 1:
            cart_object.quantity -= 1
            cart_object.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discount_price for item in cart)
        total_amount = amount + 40
        data = {
            'quantity': cart_object.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)
    

# checkout  
class CheckOutView(View):
    def get(self, request):
        user = request.user
        form = CustomerProfileForm()
        add = Customers.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        F_amount = sum(p.quantity * p.product.discount_price for p in cart_items)
        total_amount = F_amount + 40
        context = {
            'user': user,
            'form':form,
            'add':add,
            'cart_items': cart_items,
            'F_amount': F_amount,
            'total_amount': total_amount,
        }
        return render(request, "app/checkout.html", context)

    def post(self, request):
        user = request.user
        cust_id = request.POST.get("custid") 
        print("cust_id @Checkout-POST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",cust_id)
        cart_items = Cart.objects.filter(user=user)
        F_amount = sum(p.quantity * p.product.discount_price for p in cart_items)
        total_amount = F_amount + 40
        razor_amount = int(total_amount * 100)

        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_response = razorpay_client.order.create({"amount": razor_amount, "currency": "INR", "receipt": "order_rcptid_11"})
        order_id = payment_response['id']
        order_status = payment_response['status']

        if order_status == "created":
            payment = Payment(
                user=user,
                amount=total_amount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status,
            )
            payment.save()                                                  #! 
        callback_url = f"http://127.0.0.1:8000/paymentdone/?user_id={user.id}&cust_id={cust_id}"
        context = {
            "user": request.user,
            # ! pending "cust_id": cust_id,
            "callback_url": callback_url,
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "razor_amount": razor_amount,
            "order_id": order_id,
        }
        return render(request, "app/payment.html", context)
    
from django.http import HttpResponseBadRequest
@csrf_exempt
def paymentdone(request):
    user_id = request.GET.get('user_id')
    print("cust_id @ paymentdone.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",user_id)
    user = get_object_or_404(User, pk=user_id)
    cart = Cart.objects.filter(user=user_id)
    # ! pending
    """cust_id = request.GET.get('cust_id')
    print("cust_id @ paymentdone.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.",cust_id)
    customer = get_object_or_404(Customers, id=cust_id) 
    if not user_id or not cust_id:
        return HttpResponseBadRequest("User ID or Customer ID is missing.")"""

    #Verify the signature of the payment response data using Razorpay client
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    payment = None
    if request.method == "POST" and "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order_id = request.POST.get("razorpay_order_id")
        
        payment = Payment.objects.get(razorpay_order_id=order_id)
        payment.razorpay_payment_id = payment_id
        payment.signature_id = signature_id
        payment.save()

        if not verify_signature(request.POST):
            payment.razorpay_payment_status = PaymentStatus.FAILURE
            payment.save()
            return render(request, "app/order_status.html", context={"status": payment.razorpay_payment_status})
        else:
            payment.razorpay_payment_status = PaymentStatus.SUCCESS
            payment.paid = True
            payment.save()

    for c in cart:             # ! Customer id Pending
        OrderPlaced(user=user, customer=None, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
        
    return render(request, "app/order_status.html", context={"status": "Order Placed Successfully"})
# Orders success - order status
def order_success(request):
    return render(request, "app/order_status.html", locals())
