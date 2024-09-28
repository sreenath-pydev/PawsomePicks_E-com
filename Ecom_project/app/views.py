from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Products, Customers, Cart, Payment, OrderPlaced, Wishlist, ProductImage,UserProfileImg
from django.db.models import Count, Q
from .form import UserRegistrationForm, CustomerProfileForm, UserProfileImgForm
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
    if request.user.is_authenticated:
        totalitems = len(Cart.objects.filter(user=request.user))
        wishlistitems = len(Wishlist.objects.filter(user=request.user))
    Dog_product = Products.objects.filter(category__startswith='D').order_by('-id')
    Cat_product = Products.objects.filter(category__startswith='C').order_by('-id')
    return render(request, 'app/index.html',locals())

# about page
def about(request):
    if request.user.is_authenticated:
        totalitems = len(Cart.objects.filter(user=request.user))
        wishlistitems = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/about.html',locals())

# contact page
def contact(request):
    if request.user.is_authenticated:
        totalitems = len(Cart.objects.filter(user=request.user))
        wishlistitems = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/contact.html',locals())

# Retrieve products based on a specific category value and render them in a template.
class CategoryView(View):
    def get(self, request, val):
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, 'app/products.html', locals())

# product title
class CategoryTitle(View):
    def get(self, request, val):
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        product = Products.objects.filter(title=val)
        title = Products.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/products.html', locals())

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        totalitems = 0
        wishlistitems = 0
        if request.user.is_authenticated:
            in_cart = Cart.objects.filter(user=request.user, product=product)
            wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        related_products = Products.objects.filter(category=product.category).exclude(id=product.id).order_by('?') 
        other_products = Products.objects.all().exclude(id=product.id).order_by('?')[:8]
        thumbnail_images = ProductImage.objects.filter(product=product)
        return render(request, 'app/product_detail.html', locals())

# wishlist
def Wishlists(request):
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request,"app/wishlist.html",locals()) 

# Add to wishlist
def PulsWishlist(request):
    if request.method=="GET":
        prod_id = request.GET.get('prod_id')
        product = Products.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data = {
            'massage':'wishlist added successfully'
        }
    return JsonResponse(data)
# Remove option from wishlist page
def RemoveWishlist(request, prod_id):
    if request.method == "GET":
            product = Products.objects.get(id=prod_id)
            user = request.user
            Wishlist.objects.filter(user=user, product=product).delete()
    return redirect('wishlist')

# Remove From wishlist
def MinusWishlist(request):
    if request.method=="GET":
        prod_id = request.GET.get('prod_id')
        print("pppppp",prod_id)
        product = Products.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data = {
            'massage':'wishlist Removed successfully'
        }
    return JsonResponse(data)

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

#  Customer Profile
class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        all_addresses = Customers.objects.filter(user=request.user)
        latest_address = all_addresses.order_by('-id').first()
        profile_pic = UserProfileImg.objects.filter(user=request.user).first()
        return render(request, 'app/profile.html', {
            'totalitems': totalitems,
            'wishlistitems': wishlistitems,
            'latest_address': latest_address,
            'profile_pic': profile_pic,
            'messages': messages.get_messages(request),
        })

    def post(self, request):
        if request.user.is_authenticated:
            if request.POST.get('form_action') == 'update_profile_image':
                user_profile, created = UserProfileImg.objects.get_or_create(user=request.user)
                form = UserProfileImgForm(request.POST, request.FILES, instance=user_profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Congratulations! Profile image saved successfully.")
                else:
                    messages.warning(request, "Invalid input.")
                return redirect('profile')  # Redirect to avoid resubmission

            elif request.POST.get('form_action') == 'delete_profile_image':
                user_profile = UserProfileImg.objects.filter(user=request.user).first()
                if user_profile and user_profile.profile_image:
                    user_profile.profile_image.delete()  # Delete the image file from storage
                    user_profile.profile_image = None  # Set the profile_image field to None
                    user_profile.save()
                    messages.warning(request, "Profile image deleted successfully.")
                else:
                    messages.warning(request, "No profile image found to delete.")
                return redirect('profile')  # Redirect to avoid resubmission

        return redirect('profile')  # Fallback redirect

# Display the user address
def address(request):
    if request.user.is_authenticated:
        totalitems = len(Cart.objects.filter(user=request.user))
        wishlistitems = len(Wishlist.objects.filter(user=request.user))
    
    add = Customers.objects.filter(user=request.user)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode'] 
            
            # Save new address
            reg = Customers(user=user, name=name, locality=locality, city=city,
                            phone=phone, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully")
            #return redirect('some_success_url')  # Redirect after saving

    else:
        form = CustomerProfileForm()  # Create an empty form for GET requests

    context = {
        'form': form,
        'add': add,
        'totalitems': totalitems,
        'wishlistitems': wishlistitems,
    }
    
    return render(request, 'app/user_address.html', context)

# Update address
class UpdateAddressView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        add = get_object_or_404(Customers, pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/update_address.html', locals())

    def post(self, request, pk):
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
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
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(f'/product_details/{product_id}')

# Buy now
@login_required
def buy_now(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Products, id=product_id)
    
    # Check if the item already exists in the cart
    cart_item = Cart.objects.filter(user=user, product=product).first()
    
    # If the item doesn't exist in the cart, create it with quantity 1
    if not cart_item:
        Cart.objects.create(user=user, product=product, quantity=1)
    
    return redirect('cart')

# Remove from cart
def remove_from_cart(request, prod_id):
    product = get_object_or_404(Products, id=prod_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.delete()
    return redirect('/cart')

# Show cart items
def show_cart_items(request):
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    amount = np.sum([item.total_price for item in cart_items])
    total_amount = amount + 40
    return render(request, 'app/cart.html', locals())

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
        if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
        user = request.user
        form = CustomerProfileForm()
        add = Customers.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        F_amount = sum(p.quantity * p.product.discount_price for p in cart_items)
        total_amount = F_amount + 40
        context = {
            'totalitems':totalitems,
            'wishlistitems':wishlistitems,
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
        customer_name = Customers.objects.get(id=cust_id)
        contact = customer_name.phone
        mail = user.email
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
            payment.save()                                                
        callback_url = f"http://127.0.0.1:8000/paymentdone/?user_id={user.id}&cust_id={cust_id}&user={user}"
        context = {
            "user": user,
            "cust_id": cust_id,
            "customer_name": customer_name,
            "contact": contact,
            "mail": mail,
            "callback_url": callback_url,
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "razor_amount": razor_amount,
            "order_id": order_id,
        }
        return render(request, "app/payment.html", context)
    
# payment done
@csrf_exempt
def paymentdone(request):
    USER = request.GET.get('user')
    print("USER,",USER)
    user_id = request.GET.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    cart = Cart.objects.filter(user=user_id)
    cust_id = request.GET.get('amp;cust_id')
    customer = get_object_or_404(Customers, id=cust_id) 
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
    for c in cart:             
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
    return redirect('order_success')    
    
# Orders success - order status
def order_success(request):
    user = request.user
    orders = OrderPlaced.objects.filter(user=user).order_by('-order_date')
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    
    return render(request, "app/order_status.html", locals())

# Invoice generation
def invoice(request,order_id):
    order = OrderPlaced.objects.get(id=order_id)
    discount_price = order.product.discount_price
    shipping_charge = 40
    total_amount = (discount_price * order.quantity) + shipping_charge
    context = {
        'order': order,
        'total_amount': total_amount
        
        
    }
    return render(request, 'app/invoice.html', context)
  
# search 
def search_products(request):
    searched = request.GET['searched']
    print(searched)
    if searched:
        # Perform search using the query
        searched = Products.objects.filter(title__icontains=searched)
        if not searched:
            messages.success(request, "This Product Does Not Exist...Please Try Again")
            searched = Products.objects.all()
            print(searched)
    else:
        # Handle the case when the search query is not provided
        messages.success(request,"This Product Does Not Exist...Please Try Again")
        searched = Products.objects.all()
    totalitems = 0
    wishlistitems =0
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    context ={
        'totalitems':totalitems,
        'wishlistitems':wishlistitems,
        'searched': searched
    }
    return render(request, 'app/search_results.html', context)

# Dogs products & category
def dogs_products(request):
    totalitems = 0
    wishlistitems =0
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    dog_prod_Categorys = Products.objects.filter(category__startswith='D').distinct('category')
    Dog_product = Products.objects.filter(category__startswith='D').order_by('-id')
    context = {
        'totalitems':totalitems,
        'wishlistitems':wishlistitems,
        'dog_prod_Categorys': dog_prod_Categorys,
        'Dog_product': Dog_product
    }
    return render(request, 'app/category_vice_products.html',context)

# Cats products & category
def cats_products(request):
    totalitems = 0
    wishlistitems =0
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    cat_prod_Categorys = Products.objects.filter(category__startswith='C').distinct('category')
    Cat_product = Products.objects.filter(category__startswith='C').order_by('-id')
    context = {
        'totalitems':totalitems,
        'wishlistitems':wishlistitems,
        'cat_prod_Categorys': cat_prod_Categorys,
        'Cat_product': Cat_product
    }
    return render(request, 'app/category_vice_products.html', context)

# All products & category
def All_products(request):
    totalitems = 0  
    wishlistitems =0
    if request.user.is_authenticated:
            totalitems = len(Cart.objects.filter(user=request.user))
            wishlistitems = len(Wishlist.objects.filter(user=request.user))
    all_products = Products.objects.all().order_by('-id')
    all_categorys = Products.objects.all().distinct('category')
    print(all_categorys)
    context = {
        'totalitems':totalitems,
        'wishlistitems':wishlistitems,
        'all_products': all_products,
        'all_categorys': all_categorys
    }
    return render(request, 'app/category_vice_products.html', context)

# Selected Category wise products
class CategoriesViceView(View):
    def get(self, request, catg):
        # Cat Category
        if catg.startswith('C'): 
            totalitems = 0
            wishlistitems =0
            if request.user.is_authenticated:
                    totalitems = len(Cart.objects.filter(user=request.user))
                    wishlistitems = len(Wishlist.objects.filter(user=request.user))
            selected_cat_products = Products.objects.filter(category=catg)
            category_title = selected_cat_products[0].get_category_display()
            cat_prod_Categorys = Products.objects.filter(category__startswith='C').distinct('category')
            context = {
                'totalitems':totalitems,
                'wishlistitems':wishlistitems,
                'cat_prod_Categorys': cat_prod_Categorys,
                'Cat_product': selected_cat_products,
                'category_title': category_title
            }
            return render(request, 'app/category_vice_products.html', context)
        # Dog Category
        elif catg.startswith('D'): 
            totalitems = 0
            wishlistitems =0
            if request.user.is_authenticated:
                    totalitems = len(Cart.objects.filter(user=request.user))
                    wishlistitems = len(Wishlist.objects.filter(user=request.user))
            selected_dog_products = Products.objects.filter(category=catg)
            category_title = selected_dog_products[0].get_category_display()
            dog_prod_Categorys = Products.objects.filter(category__startswith='D').distinct('category')
            context = {
                'totalitems':totalitems,
                'wishlistitems':wishlistitems,
                'dog_prod_Categorys': dog_prod_Categorys,
                'Dog_product': selected_dog_products,
                'category_title': category_title
            }
            return render(request, 'app/category_vice_products.html', context)
        # All Category
        else: 
            all_products = Products.objects.filter(category=catg)
            category_title = all_products[0].get_category_display()
            all_categorys = Products.objects.all().distinct('category')
            context = {
                'all_products': all_products,
                'category_title': category_title,
                'all_categorys': all_categorys
            }
            return render(request, 'app/category_vice_products.html', context)
        

