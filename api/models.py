from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.contrib.postgres.fields import ArrayField

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    tokens = models.JSONField(default=list)
    auto = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName']
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="api_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="api_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=255, blank=False)
    goals = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    publish = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dollarValue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cadValue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numberOfStudents = models.IntegerField(default=0)
    thumbnail = models.URLField(max_length=1024, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

