from django.db import models
import datetime as dt

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', blank = True)
    img_name = models.CharField(max_length = 30)
    img_description = models.TextField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location')
    category = models.ForeignKey('Category')

    @classmethod
    def display_image(cls):
        today = dt.date.today()
        
    @classmethod
    def get_all(cls):
       images = cls.objects.order_by('-pub_date')
       return images

    @classmethod
    def filter_location(cls, location):
        images = cls.objects.filter(location__location_name__istartswith=location)
        return images
        
    @classmethod
    def filter_category(cls, category):
        images = cls.objects.filter(category__category_name__istartswith=location)
        return images

    def __str__(self):
        return self.img_name