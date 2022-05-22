from django.contrib import admin
from .models import Profile

admin.site.site_header = 'Markitten Admin Dashboard'

# Register your models here.
admin.site.register(Profile)