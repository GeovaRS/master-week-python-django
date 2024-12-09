from django.contrib import admin
from .models import TravelPackage


# Register your models here.

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'original_price', 'discounted_price')
