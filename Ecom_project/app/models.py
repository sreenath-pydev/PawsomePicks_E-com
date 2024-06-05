from django.db import models
# product categorys
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
 

# Create your models here.
class products(models.Model):
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
    