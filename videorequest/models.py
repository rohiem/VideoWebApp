from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)



    def __str__(self):
        return 'Name:{},id:{}'.format(self.title,self.id)