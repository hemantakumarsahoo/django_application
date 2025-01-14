
from django.db import models
from django.contrib.auth.models import AbstractUser
# from .models import App 

class User(AbstractUser):
    points = models.IntegerField(default=0)
# application models to store data in database
class App(models.Model):
    name = models.CharField(max_length=255)
    app_link = models.URLField(blank=True, null=True)
    sub_category = models.CharField(max_length=100, default='default_sub_category') 
    points = models.IntegerField(default=0)
    icon = models.ImageField(upload_to='app_icons/', blank=True, null=True) 
    category = models.CharField(max_length=100, default='default_category')  # Define a default here

    def __str__(self):
        return self.name
    class Meta:
        abstract = False
   #Screenshot models to  store image  in database     
class Screenshot(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, default=1)  # Assuming 1 is the ID of an existing App instance
    image = models.ImageField(upload_to='screenshots/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


