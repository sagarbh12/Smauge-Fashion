from django.db import models

# Create your models here.

#   #### Product Model ####
class productsModel(models.Model):
    Jacket_Name = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.ImageField(upload_to='images/')
    Price = models.TextField()