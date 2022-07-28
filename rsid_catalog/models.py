from operator import mod
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.
class Rsids(models.Model):
    rs_id = models.CharField(max_length=200)
    gene = JSONField() 
    created = models.DateTimeField(auto_now_add=True)
    diseases = JSONField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rsids")
    
    