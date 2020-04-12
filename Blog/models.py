from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, upload_to='posts')

    def __str__(self):
        return self.title