from django.db import models


class Leader(models.Model):
    person = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    geography = models.CharField(max_length=50)
    available = models.BooleanField(default=True)


