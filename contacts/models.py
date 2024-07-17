from django.db import models

# Create your models here.
class CustomersManagement(models.Model):
    customer = models.CharField("customers name", max_length=20, null=False)
    address = models.CharField("Adress", max_length=40, null=True)
    position = models.CharField("Position", max_length=20, null=True)
    interaction = models.FileField("Interaction", max_length=20, null=True)
    preference = models.CharField("Interaction", max_length=25, null=True)
    notes = models.TextField("Notes", max_length=150, null=True)
    campaing = models.CharField("Campaing", max_length=25, null=True, default="Null")
    email = models.EmailField("Email customer", null=False)
    phone_number = models.CharField("Customers number", max_length=14, null=False)
    status = models.CharField("Status customer", max_length=15, null=False)
    created_at = models.DateField(null=True)


    def __str__(self):
        return self.customer
    

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Customers"