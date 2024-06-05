from django.shortcuts import render
from django.views import View
from .models import products
from django.db.models import Count
# home page
def index(request):
    return render (request,'app/index.html')
# product page
class CategoryView(View):
    def get(self,request,val):
        product = products.objects.filter(category=val)
        title = products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,'app/products.html',locals())