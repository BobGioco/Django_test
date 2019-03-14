from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):#we shouldn't dirrectly inherit from the User class, otherwise database could think we have many instances of one user
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    #user model already has some default attributes(fist name,last name, password,....) and OneToOneField practicaly extend User class and we can add more attributes

    #additional
    portfolio_site=models.URLField(blank=True)#blank=True makes this field optional
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):#this will just print the user
        return self.user.username #username is default attribute of user from models module
