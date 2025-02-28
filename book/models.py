from asyncio.windows_events import NULL
from operator import truediv
from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField('Categories',max_length=100)
    slug=models.CharField(max_length=50)
    def __str__(self):
        return self.name 

    

class Book(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=75)
    cover_image=models.ImageField(upload_to='img',blank=True,null=True)
    author=models.CharField(max_length=50)
    summarry=models.TextField(max_length=200000)
    category=models.ManyToManyField(Category,related_name='books')
    pdf=models.FileField(upload_to='pdf')
    recommended_books=models.BooleanField(default=False)
    Fiction_books=models.BooleanField(default=False)
    bussiness_books=models.BooleanField(default=False)
    Health_books=models.BooleanField(default=False)
    literature_books=models.BooleanField(default=False)
    Religious_books=models.BooleanField(default=False)

    def __str__(self):
	    return self.title
		
	 



	   

       


        
    
    
    
    



