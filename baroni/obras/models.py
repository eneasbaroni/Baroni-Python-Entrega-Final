from django.db import models

class Obra(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    area = models.IntegerField()
    description = models.TextField()    
    credit = models.BooleanField()    
    image = models.ImageField(upload_to='obra_images', null=True, blank=True) #se debe instalar pillow. upload_to es donde se va a guardar la imangen en la base de datos  

    def __str__(self):
        return self.name
