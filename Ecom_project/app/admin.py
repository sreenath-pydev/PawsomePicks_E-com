from django.contrib import admin
from . models import Products,Customers,Cart,OrderPlaced,Payment,Wishlist,ProductImage,UserProfileImg

# //? model for admin panel  products details view. 
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Number of extra forms to show
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','category','product_image']
    inlines = [ProductImageInline] 

@admin.register(Customers)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','order_status','payment']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','signature_id','paid']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(UserProfileImg)
class UserProfileImgModelAdmin(admin.ModelAdmin):
    list_display = ['user','profile_image']