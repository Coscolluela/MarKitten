from django.contrib import admin
from .models import *

admin.site.site_header = 'Markitten Admin Dashboard'

class Filter(admin.ModelAdmin):
    list_display = ("user", "is_subscribed")
    list_filter = ("sex", "nationality", "birthday", "permanent_address")

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Profile, Filter)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Complaint)
admin.site.register(ProdDetails)