from django.contrib import admin
from VillaApp.models import Customer
from VillaApp.models import ImageUploader

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):list_display=['cname','cadd','phone','email','unm','pw']

admin.site.register(Customer,CustomerAdmin)
@admin.register(ImageUploader)
class ImageUploader(admin.ModelAdmin):list_display=['photo','date']