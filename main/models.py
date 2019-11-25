from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.postgres.fields import JSONField


# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with username field."""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with a given username and password."""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        Create and save a regular User with the given username and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class AppUser(AbstractUser):
    email = models.EmailField(null=True)
    username = models.CharField(max_length=50, unique=True)
    image = models.TextField(null=True,
            default='https://res.cloudinary.com/dkozdkklg/image/upload/v1565557753/cloudinary_qyi649.jpg')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_posts = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

LOCATION = (
    ('ikeja', 'Ikeja'),
    ('yaba', 'Yaba'),
    ('iyana-ipaja', 'Iyana-Ipaja'),
    ('oworonsoke', 'Oworonsoki')
)

class Review(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=200)
    street_name = models.CharField(max_length=100)
    location = models.CharField(max_length=30, choices=LOCATION)
    house_number = models.IntegerField(null=True)
    house_alias = models.CharField(max_length=100, null=True)
    landlord = models.CharField(max_length=100, null=True)
    images = JSONField(default=list)
    video = JSONField(default=list)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
