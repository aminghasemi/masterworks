from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from main.utils import ROLES, INDCHOICES, COUNTRIES_ALL, PROVINCE, COUNTRIES, USER_ROLES
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager




class User(AbstractBaseUser, PermissionsMixin):
    file_prepend = "users/profile_pics"
    username = models.CharField(max_length=100, unique=True,blank=True,null=True,verbose_name="Username")
    first_name = models.CharField(max_length=150, null=True, blank=False,verbose_name="First Name")
    last_name = models.CharField(max_length=150, null=True,  blank=False,verbose_name="Last Name")
    email = models.EmailField(max_length=255, null=True, blank=False, unique=True,verbose_name="Email")
    phone = models.CharField(max_length=16,blank=True,null=True, unique=True,verbose_name="Phone Number")
    is_active = models.BooleanField(default=True,verbose_name="Active")
    is_admin = models.BooleanField(default=False,verbose_name="Admin")
    is_staff = models.BooleanField(default=False,verbose_name="Staff")
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name="Date Joined")
    role = models.CharField(max_length=50,default="User", choices=ROLES,verbose_name="Role")
    thumbnail = models.FileField(upload_to="media",blank=True, null=True, verbose_name="Profile Picture")
    referral_code = models.CharField(max_length=100,null=True, blank=True, verbose_name="Referral Code")
    referral_share = models.SlugField(max_length=100, unique=True,blank=True,null=True,verbose_name="Refferal Sharing Code")


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-is_active"]



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


    objects = UserManager()

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name




