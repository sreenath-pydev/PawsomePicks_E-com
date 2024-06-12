from django.shortcuts import render,redirect
from django.views import View
from .models import products,customer
from django.db.models import Count
from . form import UserRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# home page
def index(request):
    return render (request,'app/index.html')
# about page
def about(request):
    return render (request,'app/about.html')
# contact page
def contact(request):
    return render (request,'app/contact.html')

# Retrieve products based on a specific category value and render them in a template.
class CategoryView(View):
    def get(self,request,val):
        product = products.objects.filter(category=val)               
        title = products.objects.filter(category=val).values('title').annotate(total=Count('title'))# ?count of how many times each title appears in the filtered products.
        return render(request,'app/products.html',locals())
    
# product title 
class CategoryTitle(View):
    def get(self,request,val):
            product = products.objects.filter(title=val) 
            title = products.objects.filter(category=product[0].category).values('title')
            return render(request,'app/products.html',locals())


# product details
class ProductDetailsView(View):
    def get(self,request,pk):
        product = products.objects.get(pk=pk)
        return render(request,'app/product_detail.html',locals())
    
# User registration form
class UserResgistrationView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'app/registration.html',locals())
    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registrated successfully")
            return redirect('login')
        else:
            messages.warning(request,"Invalid Input")

        return render(request,"app/registration.html",locals())

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
            
            reg = customer(user=user,name=name,locality=locality,city=city,phone=phone,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congradulation ! Profile saved successfully")
        else:
            messages.warning(request,"invalid input ")
        return render(request,'app/profile.html',locals())

# display the user address 
def address(request):
    add = customer.objects.filter(user=request.user)
    print(add)
    return render(request,'app/user_address.html',locals())

# update address
class UpdateAddressView(View):
    def get(self,request,pk):
        add = customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/update_address.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.phone = form.cleaned_data['phone']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Details Updated Successfully ")
            
        else:
            messages.warning(request,"INvalid Inputs")
        
        return render(request,'app/update_address.html',locals())
# delete address
class DeleteAddressView(View):
    def get(self, request, pk):
        add = customer.objects.get(pk=pk)
        add.delete()
        messages.success(request, "Address Deleted Successfully")
        return redirect('address')
    
# Handle GET requests to fetch distinct categories of products and render them in a template.
"""class CategoryView(View):
    def get(self, request, val):
        category_dict = {
            'dog': [key for key, value in CATERGORY_CHOICES if key.startswith('D')],
            'cat': [key for key, value in CATERGORY_CHOICES if key.startswith('C')],
            'other': [key for key, value in CATERGORY_CHOICES if not key.startswith('D') and not key.startswith('C')],
        }

        readable_category_dict = {key: value for key, value in CATERGORY_CHOICES}

        # Select the relevant category list
        if val == 'dog':
            categories = category_dict['dog']
            category_title = "Dog Products"
        elif val == 'cat':
            categories = category_dict['cat']
            category_title = "Cat Products"
        else:
            categories = category_dict['other']
            category_title = "Other Products"

        products_list = products.objects.filter(category__in=categories)

        return render(request, 'app/categorys.html', {
            'products': products_list,
            'category': val,
            'category_title': category_title,
            'category_dict': {key: readable_category_dict[key] for key in categories},
        })"""
