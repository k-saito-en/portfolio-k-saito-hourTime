from django.db import models

# Create your models here.

class Book(models.Model): 
    """本モデル""" 
    class Meta:
         db_table = 'book' 
         verbose_name = verbose_name_plural = '本' 

    title = models.CharField(verbose_name='タイトル', max_length=255) 

def __str__(self): 
    return self.title 