from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', blank = True)
    img_name = models.CharField(max_length = 30)
    img_description = models.TextField(max_length=50)
    location = 
    category = 



class Category(models.Model):
    category_name = models.CharField(max_length = 50)