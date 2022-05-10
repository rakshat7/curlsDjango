from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, Group

GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]

class MyUserManager(BaseUserManager):
    
    def _create_user(self,contact,password,**extrafields):
        
        if not contact:
            raise ValueError('Mobile Number is required')
        user = self.model(contact=contact,password=password,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,contact,password,**extrafields):
        
        extrafields.setdefault('is_superuser',False)
        extrafields.setdefault('role','user')
        
        user = self._create_user(contact,password,**extrafields)
        return user
    
    def create_superuser(self,contact,password,**extrafields):
        
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('role','superuser')
        
        user = self._create_user(contact,password,**extrafields)
        return user

class MyUser(AbstractBaseUser):
    
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30,null=False)
    profile_pic = models.ImageField(null=True, blank=True,default = 'user_profile_pics/default.jpg',upload_to = 'user_profile_pics')
    email = models.EmailField(unique=True,null=False)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES, default='Male')
    groups = models.ManyToManyField(Group)
    contact = models.BigIntegerField(unique=True)
    is_superuser=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    objects=MyUserManager()
    USERNAME_FIELD='contact'
    REQUIRED_FIELDS=[]
    

class Profile(models.Model):
    
    user = models.OneToOneField(MyUser, on_delete= models.CASCADE)
    image = models.ImageField(default = 'img/undraw_profile_2.svg',upload_to = 'profile_pics')
    
