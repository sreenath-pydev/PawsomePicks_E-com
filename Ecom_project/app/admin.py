from django.contrib import admin
from . models import products
# Register your models here.
@admin.register(products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','category','product_image']