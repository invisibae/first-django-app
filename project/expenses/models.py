from django.db import models

# Create your models here. # This creates a model and that model will inherit the traits of a generic model
class Summary(models.Model): # tells us generically that we are looking at a model # tells us that the model has variables with behaviors
      bioguide_id = models.CharField(max_length=7)
      office = models.CharField(max_length=500)
      program = models.CharField(max_length=500)
      category = models.CharField(max_length=500)
      year_to_date = models.DecimalField(max_digits=20, decimal_places=2)
      amount = models.DecimalField(max_digits=20, decimal_places=2)
      year = models.IntegerField()
      quarter = models.IntegerField()
