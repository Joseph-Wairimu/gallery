from django.test import TestCase

from django.test import TestCase
from .models import Category,Image

from django.test import TestCase


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Category(name = 'school')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Category))

      # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors =Category.objects.all()
        self.assertTrue(len(editors) > 0)   

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Category(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Image(name = 'testing')
        self.new_tag.save()

        self.new_article= Category(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
       Image.objects.all().delete()
       Category.objects.all().delete()
      
  
