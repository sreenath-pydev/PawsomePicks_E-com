from django.db import models
from django.contrib.auth.models import User

# product categorys model choices
CATERGORY_CHOICES=(
    ('DF','DOG_FOOD'),
    ('DT','DOG_TOYS'),
    ('DL','DOG_LEASH'),
    ('DH','DOG_HARNESS'),
    ('DB','DOG_BELT'),
    ('DBP','DOG_BATH_PRODUCTS'), 
    ('CF','CAT_FOOD'),
    ('CT','CAT_TOYS'),
    ('CL','CAT_LEASH'),
    ('CH','CAT_HARNESS'),
    ('CB','CAT_BELT'),
    ('CBP','CAT_BATH_PRODUCTS'),
    ('GP','GROOMING_PRODUCTS'),
    ('OP','OTHER_PRODUCTS')
)
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

# customer Model

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
    
# cart model
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return  self.quantity * self.product.discount_price
    
# payment model
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

# Order status model
ORDER_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('PROCESSING', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
    ('RETURNED', 'Returned'),
    ('REFUNDED', 'Refunded'),
)

# models.py

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='PENDING')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    @property
    def total_amount(self):
        return self.quantity * self.product.discount_price

    
