from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class GoUserManager(BaseUserManager):
    # defining a function or method that will create user
    def create_user(self, username, email, name, phone, password):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError('Email is required')
        if not phone:
            raise ValueError('An appropriate phone number is required')
        if not name:
            raise ValueError("Enter your correct names")

        user = self.model(
            username=username,
            email=email,
            phone=phone,
            name=name,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creating our superuser
    def create_superuser(self, username, email, phone, name, password):
        user = self.create_user(
            username=username,
            email=email,
            phone=phone,
            password=password,
            name=name
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class GoUser(AbstractBaseUser):
    username = models.CharField(verbose_name='Username', max_length=60, unique=True)
    email = models.EmailField(verbose_name='Email Address', max_length=60, unique=True)
    name = models.CharField(verbose_name='Full Name', max_length=200, unique=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=20, null=False)
    date_joined = models.DateTimeField(verbose_name='Created On', auto_now_add=True)
    profile = models.ImageField(verbose_name='Picture', upload_to=f'profiles/%Y/{username}',
                                default='profile1.png',
                                null=False)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # Fields to login to app
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    def __str__(self):
        return self.username

    objects = GoUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class GoCustomerRegistration(models.Model):
    name = models.CharField(max_length=300, verbose_name='Full name')
    type = models.CharField(max_length=20, verbose_name='Customer Type')
    destination = models.CharField(max_length=30, null=False, verbose_name='Destination')
    time_of_submission = models.DateTimeField(auto_now_add=True, null=False)
    registered_by = models.ForeignKey(GoUser, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name="Age", null=False)
    photo = models.ImageField(max_length=10000, verbose_name='Customer Picture',
                              default='profile1.png', upload_to='customers/profiles/')
    documents = models.FileField(max_length=1000, verbose_name='Documents',
                                 null=False, default=None,
                                 upload_to=f'customers/files/%Y/%m/%d')

    class Meta:
        ordering = ["time_of_submission"]

    def __str__(self):
        return '%s --- %s' % (self.name, self.documents)


class CustomerPhoto(models.Model):
    photo = models.FileField(upload_to='customers/profiles/')
    name = models.ForeignKey(GoCustomerRegistration, on_delete=models.CASCADE)
