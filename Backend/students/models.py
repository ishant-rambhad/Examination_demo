# //Backend\students\models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Add related_name to fix the clashing issue
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

# # Student Model
class StudentDetails(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    identity_proof_type = models.CharField(max_length=50)
    identity_proof_number = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    
    


    def __str__(self):
        print(self.full_name)
        print(self.email)
        print(self.password)
        print(self.date_of_birth)
        print(self.identity_proof_type)
        print(self.identity_proof_number)
        print(self.course)
        print(self.mobile_number)
        print("Data printed successfully")
        return self.email


