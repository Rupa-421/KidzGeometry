from django.db import models

# Create your models here.
class Application(models.Model):
    title=models.CharField(max_length=500)
    des=models.TextField()
    link=models.URLField()
    startdate=models.DateField()
    enddate=models.DateField()
    def __str__(self):
        return self.title

