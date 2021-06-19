from django.contrib import admin
from .models import Pizza,Size_item


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Size_item)
class PizzaAdmin(admin.ModelAdmin):
    pass