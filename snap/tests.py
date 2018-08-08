from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):

    #Set up Method
    def setUp(self):
        self.laflare=Image(img_name = 'Path', img_description = 'Road to success')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare, Image))

     # Testing Save Method
    def test_save_method(self):
        self.laflare.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

     # Testing Delete Method
    def test_delete_method(self):
        self.laflare.save_editor()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

class LocationTestClass(TestCase):

    #Set up Method
    def setUp(self):
        self.laflare=Location(location_name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare, Location))
        
class CategoryTestClass(TestCase):

    #Set up Method
    def setUp(self):
        self.laflare=Category(category_name = 'Travel')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare, Category))