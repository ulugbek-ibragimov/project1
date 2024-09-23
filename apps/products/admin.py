from django.contrib import admin
from apps.products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProduct)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProductLesson)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass