from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='teacher')
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='student')
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255 , null=True)
    file = models.FileField(upload_to='files/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name
