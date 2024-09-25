from django.db import models
from django.contrib.auth.models import User

 

# product categorys model choices
CATERGORY_CHOICES=(
    ('DF','DOG FOOD'),
    ('DT','DOG TOYS'),
    ('DL','DOG LEASH'),
    ('DH','DOG HARNESS'),
    ('DB','DOG BELT'),
    ('DBP','DOG BATH PRODUCTS'), 
    ('CF','CAT FOOD'),
    ('CT','CAT TOYS'),
    ('CL','CAT LEASH'),
    ('CH','CAT HARNESS'),
    ('CB','CAT BELT'),
    ('CBP','CAT BATH PRODUCTS'),
    ('GP','GROOMING PRODUCTS'),
    ('OP','OTHER PRODUCTS')
)
# Product model.
class Products(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    Description =  models.TextField(default='')
    composition = models.TextField(default='')
    product_app = models.TextField(default='')
    category = models.CharField(choices=CATERGORY_CHOICES,max_length=3)
    product_image = models.ImageField(upload_to='products',default='product_image')
    def __str__(self):
        return self.title
# Products  extra images
class ProductImage(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='extra_images')
    image = models.ImageField(upload_to='products/thumbnail_images/')

    def __str__(self):
        return f"{self.product.title} Image"

# cart model
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return  self.quantity * self.product.discount_price

# for customer model choices
STATE_CHOICES = (
    ('ANDAMAN AND NICOBAR ISLANDS', 'ANDAMAN AND NICOBAR ISLANDS'),
    ('ANDHRA PRADESH', 'ANDHRA PRADESH'),
    ('ARUNACHAL PRADESH', 'ARUNACHAL PRADESH'),
    ('ASSAM', 'ASSAM'),
    ('BIHAR', 'BIHAR'),
    ('CHANDIGARH', 'CHANDIGARH'),
    ('CHHATTISGARH', 'CHHATTISGARH'),
    ('DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU'),
    ('DELHI', 'DELHI'),
    ('GOA', 'GOA'),
    ('GUJARAT', 'GUJARAT'),
    ('HARYANA', 'HARYANA'),
    ('HIMACHAL PRADESH', 'HIMACHAL PRADESH'),
    ('JAMMU AND KASHMIR', 'JAMMU AND KASHMIR'),
    ('JHARKHAND', 'JHARKHAND'),
    ('KARNATAKA', 'KARNATAKA'),
    ('KERALA', 'KERALA'),
    ('LAKSHADWEEP', 'LAKSHADWEEP'),
    ('MADHYA PRADESH', 'MADHYA PRADESH'),
    ('MAHARASHTRA', 'MAHARASHTRA'),
    ('MANIPUR', 'MANIPUR'),
    ('MEGHALAYA', 'MEGHALAYA'),
    ('MIZORAM', 'MIZORAM'),
    ('NAGALAND', 'NAGALAND'),
    ('ODISHA', 'ODISHA'),
    ('PUNJAB', 'PUNJAB'),
    ('RAJASTHAN', 'RAJASTHAN'),
    ('SIKKIM', 'SIKKIM'),
    ('TAMIL NADU', 'TAMIL NADU'),
    ('TELANGANA', 'TELANGANA'),
    ('TRIPURA', 'TRIPURA'),
    ('UTTAR PRADESH', 'UTTAR PRADESH'),
    ('UTTARAKHAND', 'UTTARAKHAND'),
    ('WEST BENGAL', 'WEST BENGAL'),
    ('PUDUCHERRY', 'PUDUCHERRY'),
)

# customer Details
class Customers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    locality = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    phone = models.BigIntegerField(default=0)
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# User profile image
class UserProfileImg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(
        upload_to='profile_images/',
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
 
# store the payment details 
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    signature_id = models.CharField( max_length=128, null=True, blank=True)
    paid = models.BooleanField(default=False)

# Store purchace details after payment completed OrderPlaced 
# Order_status choices
ORDER_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('PROCESSING', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
    ('RETURNED', 'Returned'),
    ('REFUNDED', 'Refunded'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='PENDING')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    def get_progress_value(self):
        progress_values = {
            'PENDING': 25,
            'PROCESSING': 50,
            'SHIPPED': 75,
            'DELIVERED': 100,
            'CANCELLED': 100,
            'RETURNED': 100,
            'REFUNDED': 100,
        }
        return progress_values.get(self.order_status.upper(), 0)
    def get_progress_class(self):
        progress_classes = {
            'PENDING': 'bg-secondary',
            'PROCESSING': 'bg-info',
            'SHIPPED': 'bg-primary',
            'DELIVERED': 'bg-success',
            'CANCELLED': 'bg-danger',
            'RETURNED': 'bg-warning',
            'REFUNDED': 'bg-dark',
        }
        return progress_classes.get(self.order_status.upper(), 'bg-secondary')

    @property
    def total_amount(self):
        return self.quantity * self.product.discount_price

class Wishlist(models. Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
