from django.db import models

# Create your models here.
class Employee_Register(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.PositiveSmallIntegerField(unique=True)
    address = models.CharField(max_length=200)
    age = models.CharField(max_length=5)
    gender = models.CharField(
        max_length=1,
        choices=Gender,
        default=Gender.MALE,
    )
    nid = models.PositiveSmallIntegerField(unique=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name


    