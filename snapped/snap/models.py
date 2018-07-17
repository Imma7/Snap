from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', blank = True)
    img_name = models.CharField(max_length = 30)
    img_description = models.TextField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location')
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.image

class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.location_name