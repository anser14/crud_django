from django.contrib import admin
from .models import details
# Register your models here.
@admin.register(details)
class detailsAdmin(admin.ModelAdmin):
    list_display  = ('id','name','email','password')