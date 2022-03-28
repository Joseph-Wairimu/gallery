from django.test import TestCase

from django.test import TestCase
from .models import Category,Image

from django.test import TestCase


class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.category = Category(name='category')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    #testing save method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
    #testing delete method
    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==0)
    #testing update method
    def test_update_method(self):
        self.category.save_category()
        new_category = Category.objects.filter(name='category').update(name='new_category')
        categories = Category.objects.all()
        self.assertTrue(categories[0].name=='new_category')
   
 



class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.category = Category(name='category')
        self.category.save_category()
        self.image = Image(name='image',description='description',category=self.category)
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    #testing save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    #testing delete method
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
    #testing update method
    def test_update_method(self):
        self.image.save_image()
        new_image = Image.objects.filter(name='image').update(name='new_image')
        images = Image.objects.all()
        self.assertTrue(images[0].name=='new_image')

  