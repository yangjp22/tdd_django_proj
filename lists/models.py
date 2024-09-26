from django.db import models


# Create your models here.
class Item(models.Model):

    item_text = models.CharField(max_length=64)