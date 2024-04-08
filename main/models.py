from django.db import models

# Create your models here.

class Messages(models.Model):
    nickname = models.CharField(max_length=10, default="Anonymous")
    message = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)\
    
    def __str__(self):
        return self.date_created.strftime("%Y-%m-%d %I:%M %p")+ " - "+ self.nickname

