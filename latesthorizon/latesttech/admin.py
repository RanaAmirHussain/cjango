from django.contrib import admin

# Register your models here.
from .models import Image, School
admin.site.register(School)


@admin.register(Image)
class Imageadmin(admin.ModelAdmin):
    list_display=['id','photo','date']