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
    #testing get_category_by_id method
    def test_get_category_by_id(self):
        self.category.save_category()
        category = Category.get_category_by_id(self.category.id)
        self.assertTrue(category.name=='category')
    #testing get_category_by_name method
    def test_get_category_by_name(self):
        self.category.save_category()
        category = Category.get_category_by_name(self.category.name)
        self.assertTrue(category.name=='category')
    #testing get_all_categories method
    def test_get_all_categories(self):
        self.category.save_category()
        categories = Category.get_all_categories()
        self.assertTrue(len(categories)>0)


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
   
    #testing get_image_by_id method
    def test_get_image_by_id(self):
        self.image.save_image()
        image = Image.get_image_by_id(self.image.id)
        self.assertTrue(image.name=='image')
    #testing get_image_by_name method
    def test_get_image_by_name(self):
        self.image.save_image()
        image = Image.get_image_by_name(self.image.name)
        self.assertTrue(image.name=='image')
    #testing get_all_images method
    def test_get_all_images(self):
        self.image.save_image()
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)
    #testing get_image_by_category method
    def test_get_image(self):
        self.image.save_image()
        images = Image.get_image_by_category(self.category.id)
        self.assertTrue(len(images)>0)
    #testing get_image_by_category method
    def test_get_image_by_category(self):
        self.image.save_image()
        images = Image.get_image_by_category(self.category.id)
        self.assertTrue(len(images)>0)
    