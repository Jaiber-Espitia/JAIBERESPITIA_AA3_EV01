from django.db import models
from contacts.models import CustomersManagement
import datetime


# Modelo de las marcas de los productos.
class Brand(models.Model):
    name = models.CharField("Nombre", max_length=28, null=False, blank=False)
    status = models.CharField("Estado", max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
    
 
    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Brands"


# Modelo de la categoria del producto
class Category(models.Model):
    name = models.CharField("Nombre", max_length=28, null=False, blank=False)
    status = models.CharField("Estado", max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Categories"


# Modelo de la tienda del producto
class Store(models.Model):
    name = models.CharField("Nombre", max_length=30, null=False, blank=False)
    status = models.CharField("Estado", max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Stores"


# Modelo de los productos del inventario
class Product(models.Model):
    name = models.CharField("Nombre", max_length=35, null=False, blank=False)
    price = models.IntegerField("Precio", null=False, blank=False)
    quantity = models.IntegerField("Cantidad", null=False, blank=False)
    description = models.TextField("Descripcion", null=True, blank=True)
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    # Precio total
    def total_price(self):
        return self.price * self.quantity


    def __str__(self):
        return self.name


# Modelo de las ordenes de los clientes
class Order(models.Model):
    customer = models.ForeignKey(CustomersManagement, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    adress = models.CharField("Direccion", max_length=30, null=True, blank=True)
    phone = models.CharField("Telefono", max_length=15, null=True, blank=True)
    total_price = models.CharField("Telefono", max_length=15, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.product.name)