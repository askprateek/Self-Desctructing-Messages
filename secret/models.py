from django.db import models

# Create your models here.

class Secret(models.Model):
    slug = models.TextField()
    message = models.TextField()
    #time_limit = models.DateTimeField()
    status = models.BooleanField(default = 0)

    def __str__(self):
        return self.slug
