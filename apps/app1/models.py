from django.db import models

from django.contrib.auth.models import User

class Folder(models.Model):
    folder_name = models.CharField(max_length=100, unique=True)
    folder_capacity = models.PositiveIntegerField()
    floor_number = models.CharField(max_length=50)  # or IntegerField if numeric
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name


class Student(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
