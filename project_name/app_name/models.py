from django.db import models
from .countries import COUNTRIES

class Name(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100,choices=COUNTRIES)  # This field will store the selected country

    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=100)
    name_fk = models.ForeignKey(Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=100)
    name_fk = models.ForeignKey(Name, on_delete=models.CASCADE)
    block_fk = models.ForeignKey(Block, on_delete=models.CASCADE)

    def __str__(self):
        return self.name