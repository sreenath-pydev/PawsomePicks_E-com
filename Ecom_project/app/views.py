from django.shortcuts import render
from django.views import View
from .models import products,CATERGORY_CHOICES
from django.db.models import Count
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
