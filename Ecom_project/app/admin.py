from django.contrib import admin
from . models import Products, Customers, Cart, OrderPlaced, Payment, Wishlist, ProductImage, UserProfileImg
from django.utils.html import format_html

#* Products thumbnail images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Number of extra forms to show

#* Products Model Admin
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_link', 'selling_price', 'discount_price', 'category', 'product_image_display']  # Use title_link instead of title
    inlines = [ProductImageInline] 
    search_fields = ['title', 'category']
    # Custom method to display product title as clickable
    def title_link(self, obj):
        url = f"/admin/app/products/{obj.id}/change/"  
        return format_html('<a href="{}">{}</a>', url, obj.title)
    title_link.short_description = 'Title'
    
    # Custom method to display product image as clickable
    def product_image_display(self, obj):
        if obj.product_image:  
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover;" /></a>',
                obj.product_image.url,  # Link to the full-size image
                obj.product_image.url   # Thumbnail image
            )
        return '-'
    
    product_image_display.short_description = 'Product Image'

#* Customers Model Admin
@admin.register(Customers)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_link', 'name_link', 'locality', 'city', 'state', 'zipcode']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'name', 'city']

    # Custom method to make user clickable
    def user_link(self, obj):
        url = f"/admin/auth/user/{obj.user.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.user.username) if obj.user else '-'
    
    user_link.short_description = 'User'  

    # Custom method to make name clickable
    def name_link(self, obj):
        url = f"/admin/app/customers/{obj.id}/change/" 
        return format_html('<a href="{}">{}</a>', url, obj.name) if obj.name else '-'

    name_link.short_description = 'Name'  
#* Cart Model Admin
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

#* OrderPlaced Model Admin
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_link', 'customer_link', 'product_link', 'quantity', 'order_date', 'order_status', 'payment']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'customer__name', 'product__title']
    # Custom methods to display user, customer, product as clickable links
    def user_link(self, obj):
        url = f"/admin/auth/user/{obj.user.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.user.username)
    user_link.short_description = 'User'

    def customer_link(self, obj):
        url = f"/admin/app/customers/{obj.customer.id}/change/" 
        return format_html('<a href="{}">{}</a>', url, obj.customer.name)
    customer_link.short_description = 'Customer'

    def product_link(self, obj):
        url = f"/admin/app/products/{obj.product.id}/change/" 
        return format_html('<a href="{}">{}</a>', url, obj.product.title)
    product_link.short_description = 'Product'

#* Payment Model Admin
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_link', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'signature_id', 'paid']
    search_fields = [
        'user__username', 'user__first_name', 'user__last_name']
    # Custom method to make the user clickable
    def user_link(self, obj):
        url = f"/admin/auth/user/{obj.user.id}/change/"  
        return format_html('<a href="{}">{}</a>', url, obj.user.username) if obj.user else '-'

    user_link.short_description = 'User'
    
#* Wishlist Model Admin
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_link', 'product_link', 'image_display']  
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'product__title']

    # Custom method to make user clickable
    def user_link(self, obj):
        url = f"/admin/auth/user/{obj.user.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.user.username) if obj.user else '-'
    
    user_link.short_description = 'User'  # Customize column header

    # Custom method to make product clickable
    def product_link(self, obj):
        url = f"/admin/app/products/{obj.product.id}/change/" 
        return format_html('<a href="{}">{}</a>', url, obj.product.title) if obj.product else '-'
    
    product_link.short_description = 'Product'  # Customize column header

    # Custom method to display product image as clickable
    def image_display(self, obj):
        if obj.product and obj.product.product_image:  
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover;" /></a>',
                obj.product.product_image.url,  # Link to the full-size image
                obj.product.product_image.url   # Thumbnail image
            )
        return '-'
    
    image_display.short_description = 'Product Image'  

#* UserProfileImg Model Admin
@admin.register(UserProfileImg)
class UserProfileImgModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image_display']  

    # Custom method to display user profile image as clickable
    def profile_image_display(self, obj):
        if obj.profile_image:  
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover;" /></a>',
                obj.profile_image.url,  # Link to the full-size image
                obj.profile_image.url   # Thumbnail image
            )
        return '-'
    
    profile_image_display.short_description = 'Profile Image'
    