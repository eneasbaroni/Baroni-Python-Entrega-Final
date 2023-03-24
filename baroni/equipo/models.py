from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Equipo(models.Model):
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
  #phone = PhoneNumberField(max_length=100)
  bio = models.CharField(max_length=2000)
  position = models.CharField(max_length=100)
  image = models.ImageField(upload_to='equipo_images', null=True, blank=True)  #se debe instalar pillow. upload_to es donde se va a guardar la imangen en la base de datos 

  def __str__(self):
      return self.name
