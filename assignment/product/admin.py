from django.contrib import admin
from .models import productMainModel,productColour,productImage
# Register your models here.
admin.site.register(productMainModel)
admin.site.register(productColour)
admin.site.register(productImage)