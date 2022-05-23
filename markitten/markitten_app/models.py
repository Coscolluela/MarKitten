from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.fields import IntegerField
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    sex = models.CharField(max_length=100, default='Male/Female')
    birthday = models.DateField(default=datetime.date.today)
    nationality = models.CharField(max_length=100, default='Filipino')
    citizenship = models.CharField(max_length=100, default='Filipino')
    present_address = models.CharField(max_length=100, default='House No., Street Address, City, State')
    permanent_address = models.CharField(max_length=100, default='House No., Street Address, City, State')
    billing_address = models.CharField(max_length=100, default='House No., Street Address, City, State')
    shopping_address = models.CharField(max_length=100, default='House No., Street Address, City, State')
    office_address = models.CharField(max_length=100, default='House No., Street Address, City, State')
    mobile_number = models.CharField(max_length=100, default='09xx xxx xxxx')
    landline_number = models.CharField(max_length=100, default='09xx xxx xxxx')
    office_number = models.CharField(max_length=100, default='09xx xxx xxxx')
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

class BaseSupplier(models.Model):
    class Meta: 
        abstract = True
    name = models.CharField(max_length=100, null=True, blank=False)
    supplier_address = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return str(self.name)

class Supplier(BaseSupplier):
    pass

class SupplierArchive(BaseSupplier):
    pass

class BaseProduct(models.Model):
    class Meta:
        abstract=True
        
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Selling Price (in Php)')
    discount = models.DecimalField(max_digits=2, decimal_places=2, default=0, verbose_name='Percent Discount')
    quantity = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)  

    carousel_image_1 = models.ImageField(null=True, blank=False, upload_to='product_images')
    carousel_image_2 = models.ImageField(null=True, blank=True, upload_to='product_images')
    carousel_image_3 = models.ImageField(null=True, blank=True, upload_to='product_images')
    
    carousel_video_1 = models.FileField(upload_to='product_videos',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    carousel_video_2 = models.FileField(upload_to='product_videos',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return str(self.name)

class Product(BaseProduct):
    pass

class ProductArchive(BaseProduct):
    pass

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Supplier Price (in Php)')
    lead_time = models.DurationField(null=True)

    def set_leadtime(input):
        lead_time = input

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self',blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class baseReview(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

class Comment(baseReview):
    pass

class review(baseReview):
    imageReview = models.ImageField(blank=True)

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imageReview = models.ImageField(blank=True)