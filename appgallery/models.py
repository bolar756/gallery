from django.db import models
import uuid
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Shop(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_logo = models.ImageField(upload_to='logo', default='static\download (8).jpeg')
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    facebook_link=models.URLField(max_length=200)
    instagram_link=models.URLField(max_length=200)
    whatsapp_link=models.URLField(max_length=200)
    shop_bio= models.TextField()

    def __str__(self):
        return self.name
    
class ArtItems(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='art_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
