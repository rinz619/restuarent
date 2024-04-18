from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from rest_framework import serializers
# from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
    )

USER_TYPE_CHOICES = (
      (1, 'superadmin'),
      (2, 'admin'),
      (3, 'user'),
  )

STATUS_CHOICES = (
      ('unpaid', 'unpaid'),
      ('paid', 'paid'),
      ('cancelled', 'cancelled'),
  )


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.admin = 2
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = 3
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    password =  models.CharField(max_length=255, blank=True,null=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.name


    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.admin

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin





    objects = UserManager()



class Category(models.Model):
    title = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customers(models.Model):
    uniqueid = models.CharField(max_length=20,blank=False, null=False)
    name = models.CharField(max_length=20,blank=False, null=False)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Invoices(models.Model):
    uniqueid = models.CharField(max_length=20,blank=False, null=False)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.TextField(choices=STATUS_CHOICES, default='unpaid', blank=True, null=True)


@receiver(pre_save, sender=Customers)
@receiver(pre_save, sender=Invoices)
def generate_id(sender, instance, **kwargs):
    if not instance.id:
        model_class = sender
        prefix = 'CUST' if model_class == Customers else 'INVC'
        last_id = model_class.objects.all().order_by('id').last()
        try:
            if last_id:
                last_id_int = int(last_id.uniqueid.split('_')[-1])
                new_id = f'{prefix}_{last_id_int + 1:04d}'
            else:
                new_id = f'{prefix}_0001'
        except:
            new_id = f'{prefix}_0001'
        instance.uniqueid = new_id
