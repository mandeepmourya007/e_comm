from django.db import models

class book(models.Model):
    title=models.CharField(max_length=32)
    author_name=models.CharField(max_length=32)
    detail=models.TextField()
  
    def __str__(self):
        return self.title
