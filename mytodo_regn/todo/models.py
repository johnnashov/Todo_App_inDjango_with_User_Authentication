from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomerToDoItem(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
  content = models.CharField(max_length=1000)
  priority = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.content

