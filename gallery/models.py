from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80 , unique=True)


    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to ='artciles',blank =False)
    name = models.CharField(max_length=80)
    description = models.TextField()
    author = models.CharField(max_length=70, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  