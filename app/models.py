from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Email not given')
        
        #^-----normalising email
        NE = self.normalize_email(email)
        UPO = self.model(email=NE, first_name=first_name,last_name=last_name)
        
        #^-----Hashing password
        UPO.set_password(password)
        UPO.save()
        return UPO
    
    def create_superuser(self,email,first_name,last_name,password):
        UPO = self.create_user(email,first_name,last_name,password)
        
        #^-----changing the permissions for Superuser
        UPO.is_staff=True
        UPO.is_superuser=True
        UPO.save()
        
        
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    #^-----Permissions for user and superuser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    #^-----connecting with UserProfileManager
    objects = UserProfileManager()
    
    #^-----using email as authenication
    USERNAME_FIELD = 'email'
    
    #^-----creating mandatory fields
    REQUIRED_FIELDS= ['first_name', 'last_name']
    

        



