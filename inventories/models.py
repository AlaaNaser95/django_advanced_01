from django.db import models
from stores.models import Store

# Create your models here.
class Inventory(models.Model):
	name=models.CharField(max_length=200)
	store= models.ForeignKey(Store, on_delete=models.CASCADE, default=1)
	is_empty=models.BooleanField()
	last_updated=models.DateTimeField(auto_now=True)