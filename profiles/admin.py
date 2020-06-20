from django.contrib import admin
from .models import profile
# Register your models here.

# class profileadmin(admin.ModelAdmin):
#     list_display=('title','date_created')

admin.site.register(profile)