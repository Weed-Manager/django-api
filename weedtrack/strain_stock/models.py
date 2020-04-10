from django.db import models
from weedtrack.users.models import User

# Create your models here.

class StrainStock(models.Model):
    strain_name = models.CharField(max_length=255, null=False)
    quantity = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class StrainOperation(models.Model):
    strain = models.ForeignKey(StrainStock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.FloatField()
