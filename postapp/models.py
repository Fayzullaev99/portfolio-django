from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  image = models.FileField(upload_to="post-images")
  created_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    app_label = 'postapp'