from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid  # Import the UUID module
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    

    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=8, unique=True, editable=False) 
    grade = models.CharField(max_length=10)
    # Add other student-specific fields
    def save(self, *args, **kwargs):
        if not self.student_id:
            # Generate a unique 8-character student ID
            self.student_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)

    def __self__(self):
        return self.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    staff_role = models.CharField(max_length=50)
    # Add other admin-specific fields
    def __self__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for the user profile, e.g., profile_picture, bio, etc.
    # Example:
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    student_id = models.CharField(max_length=8, unique=True, null=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)  # Indicates book availability
    available_copies = models.PositiveIntegerField(default=0)  # This field stores the number of available copies
    category = models.ManyToManyField(Category, related_name='books', blank=True)

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


