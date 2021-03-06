from django.db import models
import datetime as dt

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    # image = models.ForeignKey(Image)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length = 50)
    # image = models.ForeignKey(Image)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', blank = True)
    img_name = models.CharField(max_length = 30)
    img_description = models.TextField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.img_name
        
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        specific_image = cls.objects.get(id = id)
        return specific_image

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
        images = cls.objects.filter(category__category_name__istartswith=category)
        return images

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(img_name__icontains=search_term)
        return images

    