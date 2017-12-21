from django.db import models


# Create your models here.
class Entry(models.Model):
    image = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    nasa_id = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='entries', on_delete=models.CASCADE, null=True)
