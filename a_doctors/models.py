from django.db import models
from django.contrib.auth.models import User # chat

# Create your models here.
class User(models.Model):
    p_k=models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)  # chat
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    password=models.CharField(max_length=100)
   
    profile_pic=models.ImageField(upload_to="profile_pic/",default="")
        
    def __str__(self):
        return self.fname
    
# chat /*
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.TextField()   # */