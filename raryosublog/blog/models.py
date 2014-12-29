from django.db import models
from datetime import datetime

# Create your models here.
class blogdata(models.Model):
  title = models.CharField(max_length=512)
  text = models.TextField()
  date = models.DateTimeField(default=datetime.now)
