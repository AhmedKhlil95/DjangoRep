from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserprofileInfo(models.Model):

    models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True, max_length=200)
    profile_pic = models.ImageField( upload_to="profile_pics",blank = True)
    def __str__(self):
        return self.user.username
