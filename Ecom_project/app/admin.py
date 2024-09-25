from django.contrib import admin
from . models import Products,Customers,Cart,OrderPlaced,Payment,Wishlist,ProductImage,UserProfileImg

# Products thumbnail images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Number of extra forms to show

# Products Model Admin
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','category','product_image']
    inlines = [ProductImageInline] 
    search_fields = ['title','category']

# Customers Model Admin
@admin.register(Customers)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state','zipcode']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'name', 'city']
# Cart Model Admin
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

# OrderPlaced Model Admin
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','order_status','payment']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'customer__name', 'product__title']
# Payment Model Admin
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','signature_id','paid']
    search_fields = [
        'user__username','user__first_name','user__last_name',]
# Wishlist Model Admin
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

# UserProfileImg Model Admin
@admin.register(UserProfileImg)
class UserProfileImgModelAdmin(admin.ModelAdmin):
    list_display = ['user','profile_image']