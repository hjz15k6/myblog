from django.db import models

# Create your models here.
class article(models.Model):
	title = models.CharField(max_length = 140)
	date = models.DateTimeField(auto_now_add = True)
	content = models.TextField(blank = True, null = True)