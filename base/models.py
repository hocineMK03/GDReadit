from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Place(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.TextField(max_length=20)
    desc=models.TextField(max_length=200,null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class Messages(models.Model):
      host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
      where=models.ForeignKey(Place,on_delete=models.CASCADE)
      body=models.TextField(max_length=200)
      date_created=models.DateTimeField(auto_now=True)
      def __str__(self):
           return self.body[0:50]



