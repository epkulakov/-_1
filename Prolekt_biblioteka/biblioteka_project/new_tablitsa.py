from django.db import models

title = models.CharField(max_length=200)
author = models.CharField(max_length=100)
opisanie = models.CharField(max_length=10000)
date = models.DateField()