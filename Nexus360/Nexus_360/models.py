from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


#---------Categories---------#

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')


class News_Post(models.Model):
    title=models.CharField(max_length=100)
    News_content=models.TextField()
    date=models.DateField(default='DEFAULT VALUE')
    #post_date=models.DateField(auto_now_add=True)

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=30,default='Politics')

    def __str__(self):
        return self.title + ' | '+ str(self.author)
    def get_absolute_url(self):
        return reverse('home')
