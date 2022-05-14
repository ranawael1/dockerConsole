from django.db import models
from django.contrib.auth.models import User 


class Container(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'tag',)
    def __str__(self):
        return self.name



