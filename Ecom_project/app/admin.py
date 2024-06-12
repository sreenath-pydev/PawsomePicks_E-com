from django.contrib import admin
from . models import products,customer

# //? model for admin panel  products details view. 
@admin.register(products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','category','product_image']

@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state','zipcode']