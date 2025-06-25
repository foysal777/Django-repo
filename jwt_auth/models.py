from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    otp = models.CharField(max_length=6, blank=True, null=True)
    subscribed = models.BooleanField(default=False)

    def __str__(self):  
        return self.user.username
    
class Students(models.Model):
    name  = models.CharField(max_length=100)
    age = models.ImageField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name  = models.CharField(max_length=100)
    age = models.ImageField()
    profession = models.CharField(max_length=40)
    dept = models.CharField(max_length=70)
    
    
    def __str__(self):
        return self.name