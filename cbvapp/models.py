from django.db import models
# import reverse
from django.urls import reverse

# Create your models here.
class School (models.Model):
    # fields
    name = models.CharField(max_length=255, null=False)
    principal = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    # str
    def __str__(self):
        return self.name
    # get_absolute_url()
    def get_absolute_url(self):
        return reverse("school-list")