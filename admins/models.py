from django.db import models
# Create your models here.
  
class AppAdmin(models.Model):
    app_name = models.CharField(max_length=100)
    app_link = models.CharField(max_length=100)
    app_category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    points = models.IntegerField(default=1)
    app_icon = models.ImageField(upload_to='img')

    def __str__(self):
        return self.app_name
