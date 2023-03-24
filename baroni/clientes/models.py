from django.db import models

class Cliente(models.Model):
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  credit = models.BooleanField()     
  active = models.BooleanField()

  def __str__(self):
      return self.name

