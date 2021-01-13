from django.db import models

# Create your models here.
class portfolio(models.Model):
    title=models.CharField(max_length=100)
    disc=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)
