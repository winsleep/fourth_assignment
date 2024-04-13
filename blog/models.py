from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)#각각의 데이터를 저 형태로 저장해
    image = models.ImageField(upload_to="blog/", null =True)