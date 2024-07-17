from django.contrib import admin
from inventory.models import (
    Brand,
    Category,
    Store,
    Order,
    Product
)

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(Product)
