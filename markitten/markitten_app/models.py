from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
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
