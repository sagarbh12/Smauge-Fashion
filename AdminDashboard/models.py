from django.db import models

# Create your models here.
<<<<<<< HEAD

#   #### Product Model ####
class productsModel(models.Model):
    Jacket_Name = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.ImageField(upload_to='images/')
    Price = models.TextField()
=======
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154
