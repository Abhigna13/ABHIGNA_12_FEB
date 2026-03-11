from django.db import models


class Student(models.Model):

    # Gender Choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # Blood Group Choices
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    # ✅ ADD THIS FIELD
    
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    branch = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    phone = models.CharField(max_length=10)

    # ✅ This controls how name appears in admin & shell
    def __str__(self):
        return self.name
    
    