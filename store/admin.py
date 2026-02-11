from django.contrib import admin

from .models import *

admin.site.register(Seller)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(CategoryAttribute)
admin.site.register(Product)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductVariant)
admin.site.register(VariantAttributeValue)
admin.site.register(ProductImage)
admin.site.register(AttributeRequest)
admin.site.register(Products)