from django.db import models

# Create your models here.
class Subscribe_model(models.Model):
    Email =  models.EmailField(max_length = 50)
    Name = models.CharField(max_length= 50, default = 'none')

    def __str__(self):
        return self.Email
