from django.db import models


class delete(models.Model):
    nomer = models.CharField(max_length=100)

    def __str__(self):
        return self.username