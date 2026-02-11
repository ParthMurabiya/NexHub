from django.db import models
from login.models import Account,TimeStampedModel


class Seller(TimeStampedModel):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)

    def __str__(self):
        
        return self.store_name

from django.db import models

class Company(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ImageField(
        upload_to='company_logos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
    
class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoryAttribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'attribute')

    def __str__(self):
        return f"{self.category} - {self.attribute}"


class Product(TimeStampedModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
  

    def __str__(self):
        return self.title
    
class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('product', 'attribute')

    def __str__(self):
        return f"{self.attribute}: {self.value}"

class ProductVariant(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} variant"

class VariantAttributeValue(TimeStampedModel):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('variant', 'attribute')

class ProductImage(TimeStampedModel):
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='product_images/')

class AttributeRequest(TimeStampedModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reason = models.TextField()
    approved = models.BooleanField(default=False)
  

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100)
    prise=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')